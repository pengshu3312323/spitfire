#! usr/bin/env python3
# -*- coding:utf-8 -*-


class BaseItemFactory:
    def new_item(self, name, cost, member_list):
        from .func import AaItem
        item = AaItem(name, cost, member_list)
        return item
