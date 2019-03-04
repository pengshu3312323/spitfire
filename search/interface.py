#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from abc import ABCMeta, abstractmethod


class SearchAbstract(metaclass=ABCMeta):
    @property
    def keywords(self):
        return self._keywords

    @keywords.setter
    def keywords(self, value):
        if isinstance(value, str):
            self._keywords = value
        else:
            raise TypeError('Keywords must be str')

    @property
    def search_target(self):
        return self._search_target

    @search_target.setter
    def search_target(self, value):
        self._search_target = value

    @abstractmethod
    def keywords_handle(self):
        pass
