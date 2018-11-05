#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from enum import Enum


class SearchEngineConfig:
    # 支持的搜索引擎，其中Bing为国内版
    SEARCH_PALTFORM = Enum(
        'SearchPlatform', (
            'Baidu', 'Google', 'Bing',
            )
    )

    SEARCH_URL = {
        'Baidu': 'https://www.baidu.com/s?wd=',
        'Google': 'https://www.google.com/search?q=',
        'Bing': 'https://cn.bing.com/search?q=',
    }


class MovieSearchConfig:
    SEARCH_PALTFORM = Enum(
        'SearchPlatform', (
            'Piratebay',
        )
    )
