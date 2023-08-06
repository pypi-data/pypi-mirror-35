import time
from urllib import parse


class Utils:

    @staticmethod
    def build_get_url(base, path, query={}):
        if '?' in path:
            tmp = path.split('?')
            path = tmp[0]

        query['t'] = time.time()
        return parse.urljoin(base, "%s?%s" % (path, parse.urlencode(query)))
