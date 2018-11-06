#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest

from search.func import WebSearch


class TestWebSearch(unittest.TestCase):
    def setUp(self):
        print('Setup')
        self.TEST_KEYWORDS = 'mazda volvo'

    def tearDown(self):
        print('Teardown')

    def test_1(self):
        websearch = WebSearch()
        url = websearch.get_redirect_url(self.TEST_KEYWORDS, 1)
        print(url)
        self.assertTrue(url)

    def test_2(self):
        websearch = WebSearch()
        url = websearch.get_redirect_url(self.TEST_KEYWORDS, 2)
        print(url)
        self.assertTrue(url)

    def test_3(self):
        websearch = WebSearch()
        url = websearch.get_redirect_url(self.TEST_KEYWORDS, 3)
        print(url)
        self.assertTrue(url)
