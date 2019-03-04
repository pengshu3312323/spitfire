#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from search import handlers as search_handlers


handlers = [
    (r'/search/web/?', search_handlers.WebSearchHandler),
    (r'/search/google/?', search_handlers.GoogleSearchHandler),
]