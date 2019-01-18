#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from account.interface import AccountAbstract, MemberAbstract, ItemAbstract


class AaAcount(AccountAbstract):
    '''
    纯AA制账目
    '''
    def member_register(self, member):
        # TODO 钱怎么处理
        self._member_list.append(member)
        self._member_num += 1

    def member_remove(self, member):
        # TODO 钱怎么处理
        if member in self._member_list:
            self._member_list.remove(member)
        else:
            raise ValueError('成员中没有这个人')

    @property
    def member_list(self):
        if self._member_list:
            print('No member in this account')
            return 0
        else:
            for m in self._member_list:
                print(m)

    # 消费项目处理
    def create_item(self, name, cost, member_list, operator=None):
        item = self._item_factory.new_item(name, cost, member_list)
        self._item_list.append(item)
        self._total_money_update(item)


class AaMember(MemberAbstract):
    '''
    一群好朋友
    '''
    pass


class AaItem(ItemAbstract):
    '''
    好朋友一起玩的东西
    '''
    def split_cost(self):
        for member in self.member_list:
            member.add_item(self)
