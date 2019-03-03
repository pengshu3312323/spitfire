#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from tornado.web import RequestHandler

from search.func import WebSearch, GoogleSearch


class WebSearchHandler(RequestHandler):
    def get(self):
        web_search = WebSearch()
        keywords = self.get_argument('keywords')
        search_target = int(self.get_argument('search_target', 1))
        url = web_search.get_redirect_url(keywords, search_target)
        self.redirect(url)


class GoogleSearchHandler(RequestHandler):
    def get(self):
        keywords = self.get_argument('keywords')
        page_num = self.get_argument('page_num')
        google_search = GoogleSearch()
        res = google_search.get_search_result(keywords, page_num)
        '''
        res = {
            'success': True,
            'msg': 'Sorry,出现故障了',
            'data': [
                {"search_type": "g", "keyword": "python", "page_num": 0, "title": "Python 1", "source": "http://www.runoob.com/python/python-intro.html", "des": "<div><span>这是详情<em>1<em></span></div>"},
                {"search_type": "g", "keyword": "python", "page_num": 0, "title": "Python 2", "source": "http://www.runoob.com/python/python-intro.html", "des": "<div><span>这是详情<em>2<em></span></div>"},
            ]
        }
        '''
        self.set_header('Content-Type', 'application/json;charset=utf-8')
        self.write(res)
        # self.render('templates/search_results.html', res=res)
