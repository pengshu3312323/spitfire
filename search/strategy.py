#! /usr/bin/env python3
# -*- coding:utf-8 -*-
import json

from throttle.throttle.client import SearchClient
from cache import cache_control
from log import logger


class KeywordsOperate:
    def __init__(self, keywords, search_target):
        self.search_target = search_target
        self.keywords = keywords

    def words_split(self):
        return WordsSplit.symbol_split(self.keywords)


class WordsSplit:
    @staticmethod
    def symbol_split(keywords):
        # 目前只按空格来分段
        return keywords.split(' ')

    @staticmethod
    def smart_split(keywords):
        pass

    @staticmethod
    def do_nothing(keywords):
        return [keywords, ]


class GoogleSearchClient:
    def __init__(self):
        self.client = SearchClient()

    # @cache_control(100)
    def search(self, keyword, pn):
        res = {
            'success': False,
            'msg': '',
            'data': None,
        }
        try:
            data = self.client.send(keyword, pn)
        except Exception as e:
            logger.error(e, exc_info=True)
            data = 0

        if data == 0:
            res['success'] = False
            res['msg'] = 'Sorry，出现故障了'
        else:
            res = data
        return res
