import queue,traceback,simplejson,pyquery,logging,time

from .fetcher import Fetcher

logger = logging.getLogger('SimpleSpider')


class BaseSpider:

    def __init__(self, options={}):
        '''
        option指定相关配置参数
        :param options:
            * enable_session: 开启抓取器的session，将自动保存IP等
            * proxy_list : 代理列表
            * debug_proxy: 开启调试代理。debug_proxy有值的情况下，会忽略proxy_list选项
        '''

        self.task_queue = queue.Queue()
        self.fetcher = Fetcher(options)

    def run(self):
        self.start()

        while True:
            try:
                task = self.task_queue.get_nowait()
                self._do_task(task)

                time.sleep(1)
            except queue.Empty:
                logger.info("task queue is empty now")
                break
            except Exception as e:
                # 其他异常
                raise e



    def crawl(self,url, callback, method = 'GET', data = {}, headers={}, cookies = {},options={}, save={}):
        if not url or not callback:
            raise Exception("Url and callback should be set")

        # 先测试一下是否
        cb_func = getattr(self,callback.__name__)
        if not callable(cb_func):
            raise Exception("%s is not callback", callback.__name__)

        task = {
            'url': url,
            'callback': callback.__name__,
            'method': method,
            'data': data,
            'cookies': cookies,
            'headers': headers,
            'options': options,
            'save': save
        }
        logging.info("New crawl task: url = %s, callback = %s" %(url, cb_func))
        self.task_queue.put(task)

    def _do_task(self,task):
        self.fetcher.pick_new_proxy()

        url = task.get('url')
        callback = task.get('callback')
        headers = task.get('headers',{})
        options = task.get('options',{})
        method = task.get('method','GET')
        data = task.get('data',{})
        cookies = task.get('cookies',{})
        save = task.get('save',{})

        # 判断是否需要限流
        last_execute = task.get('last_execute', 0)
        current_proxy = self.fetcher.current_proxy()
        if time.time() - last_execute <= self.throttle(url, current_proxy):
            # 命中节流
            logger.debug("Hit throttling, try next time. url = %s, proxy = %s" % (url, current_proxy) )
            self.task_queue.put(task) # 重新放入队列即可，不额外处理
            return

        data_type = options.get('content-type','html')
        logger.debug("Start crawling %s with callback = %s and content-type = %s" % (url, callback, data_type))
        err = None
        content = ''
        try:
            logger.info("Do fetching url: %s" % url)
            result = self.fetcher.fetch(url, method= method, headers= headers, cookies = cookies, data= data)
            status_code = result.get('status_code',404)
            reason = result.get('reason','')
            content = result.get('content')
            logger.debug("Got status code %d " % status_code)

            if status_code == 200:
                pass
            else:
                err = SpiderError(
                    status_code=status_code,
                    reason=reason,
                    url=url,
                    content=content,
                    proxy=self.fetcher.current_proxy())

        except Exception as e:
            err = SpiderError(
                status_code = 0,
                reason = str(e),
                url = url,
                content = None,
                proxy = self.fetcher.current_proxy()
            )

        cb = getattr(self,callback)
        if callable(cb):
            ret = True
            try:
                if err:
                    logger.warning("Found error when fetching %s, status code = %s, and err reason = %s " %(url, err.status_code, err.reason))
                    ret = cb(err, SpiderResponse(err.reason, type= 'text', task= task))
                else:
                    ret = cb(None, SpiderResponse(content, type= data_type,task= task ))
            except Exception as e:
                logger.error('Error when process fetch result: %s' % traceback.format_exc())

            if ret is True:
                self.evaluate_proxy(self.fetcher.current_proxy(), True)
            else:
                # 返回False，表示处理失败，包括返回了爬虫页面之类，这个情况下，需要给代理扣分，并且稍后重试
                self.evaluate_proxy(self.fetcher.current_proxy(), False)
                self.retry_task(task)

    def retry_task(self,task):
        retry = task.get('retry', 0)
        options = task.get('options', {})
        max_reties = options.get('retry', 3)  # 重试次数

        if retry >= max_reties:
            logger.info("Skip task because retry max count, url= %s" % task.get('url'))
        else:
            retry += 1
            task.update(
                {
                    'retry': retry,
                    'last_execute': time.time()
                 }
            )
            self.task_queue.put(task)

    def evaluate_proxy(self,proxy, status):
        if status:
            self.fetcher.inc_proxy_score(proxy)
        else:
            self.fetcher.desc_proxy_score(proxy)


    def throttle(self,url,proxy):
        return 1

    def start(self):
        logger.warn("start must be implement")


class SpiderError:
    def __init__(self, status_code,reason, url, content, proxy):
        self.status_code = status_code
        self.reason = reason
        self.url = url
        self.content = content
        self.proxy = proxy


class SpiderResponse:
    def __init__(self, content, type='text', task={}):
        self.content = content
        self.json = None
        self.doc = None
        self.save = task.get('save',{})
        self.url = task.get('url')
        self.task = task

        if type == 'text':
            pass
        elif type == 'json':
            self.json = simplejson.loads(self.content)
        elif type == 'html':
            self.doc = pyquery.PyQuery(content)
        else:
            # 默认使用html来解析
            self.doc = pyquery.PyQuery(content)
