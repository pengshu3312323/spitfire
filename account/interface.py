#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from abc import ABCMeta, abstractmethod
from decimal import Decimal, getcontext

from account.factory import BaseItemFactory


class AccountAbstract(metaclass=ABCMeta):
    '''
    账目基类
    '''
    def __init__(self, account_name, account_desc):
        self._member_list = list()
        self._member_num = len(self._member_list)

        self._item_list = list()
        self._item_num = len(self._item_list)

        self.account_name = account_name
        self.account_desc = account_desc

        self._operation_log = list()
        self._item_factory = BaseItemFactory()
        self._total_money = Decimal('0.00')
        self._average_money = Decimal('0.00')

    # 账目名称和描述
    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        try:
            account_name = str(account_name)
        except Exception:
            raise TypeError('需要字符串')
        if len(account_name) > 20:
            raise ValueError('请勿大于20个字符')

        self._account_name = account_name

    @property
    def account_desc(self):
        return self._account_desc

    @account_desc.setter
    def account_desc(self, account_desc):
        try:
            account_name = str(account_desc)
        except Exception:
            raise TypeError('需要字符串')
        if len(account_name) > 50:
            raise ValueError('请勿大于50个字符')

        self._account_desc = account_desc

    # 账目总价处理
    @property
    def total_money(self):
        return self._total_money

    @total_money.setter
    def total_money(self, money):
        print('不能直接修改总金额!')
        return 0

    def _total_money_update(self, item_money):
        try:
            item_money = str(item_money)
        except Exception:
            raise TypeError('Money must be a str')

        item_money = Decimal(item_money)
        self._total_money += item_money

    # 账目参考均价处理
    @property
    def average_money(self):
        return str(self._average_money)

    @average_money.setter
    def average_money(self, value):
        print('不能直接修改平均金额!')
        return 0

    def _average_money_update(self):
        getcontext.prec = 2
        self._average_money = self._total_money / self._member_num
        return str(self._average_money)

    # 账目内成员处理
    @abstractmethod
    def member_register(self, member):
        pass

    @abstractmethod
    def member_remove(self, member):
        pass

    @property
    def member_list(self):
        # TODO 试试迭代器模式？
        if not self._member_list:
            print('No member in this account')
            return 0
        else:
            for m in self._member_list:
                print(m)

    # 消费项目处理
    @abstractmethod
    def create_item(self, name, money, member_list, operator):
        pass


class MemberAbstract(metaclass=ABCMeta):
    '''
    分账成员基类
    '''
    @abstractmethod
    def __init__(self, name):
        self.name = name

        self._cost = Decimal('0.00')
        self._item_list = list()

    # 单个成员总账目
    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        print('不能直接修改金额!')
        return 0

    def _cost_add(self, item_aver_money):
        try:
            item_aver_money = str(item_aver_money)
        except Exception:
            raise TypeError('Money must be a str')

        self._cost += item_aver_money

    def _cost_reduce(self, item_aver_money):
        try:
            item_aver_money = str(item_aver_money)
        except Exception:
            raise TypeError('Money must be a str')

        self._cost -= item_aver_money

    # 单个成员所参与的项目列表
    def add_item(self, item):
        self._item_list.append(item)
        self._cost_add(item.aver_money)

    def remove_item(self, item):
        if item in self._item_list:
            self._item_list.remove(item)
            self._cost_reduce(item.aver_money)

    def display_item(self):
        if self._item_list:
            pass
        else:
            return '还没有消费项目'


class ItemAbstract(metaclass=ABCMeta):
    '''
    消费项目基类
    '''
    pass
