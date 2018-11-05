#! /usr/bin/env python3
# -*- coding:utf-8 -*-


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
