#! /usr/bin/env python3
# -*- coding:utf-8 -*-


class KeywordsOperate:
    def __init__(self, search_target):
        self.search_target = search_target

    def words_split(self):
        return WordsSplit.do_nothing()

    def gen_url(self):
        pass


class WordsSplit:
    @staticmethod
    def symbol_split(keywords):
        pass

    @staticmethod
    def smart_split(keywords):
        pass

    @staticmethod
    def do_nothing(keywords):
        return [keywords, ]
