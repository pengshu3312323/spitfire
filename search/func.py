#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from .strategy import KeywordsOperate


class SearchAbstract:
    def __init__(self, keywords, search_target):
        self.keywords = keywords
        self.search_target = search_target


class WebSearch(SearchAbstract):
    '''
    百度、谷歌、bing搜索
    '''
    def keywords_handle(self):
        keywords_operator = KeywordsOperate(self.search_target)
        self.keywords_list = keywords_operator.words_split()

    def gen_url(self):
        pass


class MovieSearch(SearchAbstract):
    '''
    搜电影
    '''
