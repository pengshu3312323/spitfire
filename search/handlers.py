#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from tornado.web import RequestHandler

from search.func import WebSearch


class WebSearchHandler(RequestHandler):
    def get(self):
        websearch = WebSearch()
        keywords = self.get_argument('keywords')
        search_target = int(self.get_argument('search_target', 1))
        url = websearch.get_redirect_url(keywords, search_target)
        self.redirect(url)
