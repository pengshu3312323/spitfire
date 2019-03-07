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
        keywords = self.get_argument('keywords', default=None)
        page_num = self.get_argument('page_num', default=0)
        json = self.get_argument('json', default=None)

        if not keywords:
            self.send_error(400)

        google_search = GoogleSearch()
        res = google_search.get_search_result(keywords, page_num)
        '''
        res = {
            'success': True,
            # 'msg': 'Sorry,出现故障了',
            'data': [
                {
                    "search_type": "g",
                    "keyword": "google",
                    "page_num": 1,
                    "title": "Google",
                    "source": "http://www.google.cn/",
                    "des": "<span class=\"st\">Search the world's information, including webpages, images, videos and more. <em>Google</em> has many special features to help you find exactly what you're looking ...</span>"
                },
            ]
        }
        '''
        if json is not None:
            self.set_header('Content-Type', 'application/json;charset=utf-8')
            self.write(res)
        else:
            self.render('templates/search_results.html', res=res)
