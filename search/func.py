#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from search.config import SearchEngineConfig, MovieSearchConfig
from search.strategy import KeywordsOperate
from search.interface import SearchAbstract


class WebSearch(SearchAbstract):
    '''
    百度、谷歌、bing搜索
    '''
    @property
    def search_target(self):
        return self._search_target

    @search_target.setter
    def search_target(self, value):
        '''验证搜索引擎类型'''
        if not isinstance(value, int):
            raise TypeError('Input search target must be an integer')
        try:
            self._search_target = SearchEngineConfig.SEARCH_PALTFORM(value)
        except ValueError:
            raise ValueError('Unsupported search engine')

    def keywords_handle(self):
        '''处理关键字'''
        keywords_operator = KeywordsOperate(self.keywords, self.search_target)
        self.keywords_list = keywords_operator.words_split()

    def gen_url(self):
        '''拼装成跳转url'''
        search_url = SearchEngineConfig.SEARCH_URL[self.search_target.name]
        return search_url + '+'.join(self.keywords_list)

    def get_redirect_url(self, keywords, search_target):
        self.search_target = search_target
        self.keywords = keywords
        self.keywords_handle()
        return self.gen_url()


class MovieSearch(SearchAbstract):
    '''
    搜电影
    '''
