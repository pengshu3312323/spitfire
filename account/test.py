#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from account.interface import ItemAbstract


class ItemTest(ItemAbstract):
    def __init__(self):
        print('Got instance')
