#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import unittest
import sys
import os

BASE_DIR = os.path.dirname(os.path.dirname(__name__))
sys.path.append(BASE_DIR)

from account.func import AaMember, AaItem


class ItemMemberTest(unittest.TestCase):
    def setUp(self):
        print('Item和Member测试')
        self.member_list = []
        self.item_list = []

    def test_a_member_1(self):
        p_s = AaMember(name='ps_sqq')
        print('成员:{}建立完成'.format(p_s.name))
        self.member_list.append(p_s)
        self.assertEqual(p_s.cost, '0.00')

    def test_b_item_1(self):
        p_s = AaMember(name='ps_sqq')
        self.member_list.append(p_s)

        f_r = AaMember(name='fjx_rj')
        self.member_list.append(f_r)

        x_g = AaMember(name='xlx_gtl')
        self.member_list.append(x_g)

        item_1 = AaItem(name='住宿', cost=720, member_list=self.member_list)
        self.item_list.append(item_1)
        item_2 = AaItem(name='零食', cost=170, member_list=self.member_list)
        self.item_list.append(item_2)
        item_3 = AaItem(name='下山观光车', cost=180, member_list=self.member_list)
        self.item_list.append(item_3)
        item_4 = AaItem(name='去车票', cost=414, member_list=self.member_list)
        self.item_list.append(item_4)
        item_5 = AaItem(name='理县到毕棚沟包车', cost=100, member_list=self.member_list)
        self.item_list.append(item_5)
        item_6 = AaItem(name='回成都车票', cost=468, member_list=self.member_list)
        self.item_list.append(item_6)
        item_7 = AaItem(name='牛肉汤锅', cost=380, member_list=self.member_list)
        self.item_list.append(item_7)
        item_8 = AaItem(name='门票', cost=510, member_list=self.member_list)
        self.item_list.append(item_8)
        item_9 = AaItem(name='草帽', cost=248, member_list=self.member_list)
        self.item_list.append(item_9)

        for i in self.item_list:
            print('{}: {}'.format(i.name, i.cost))
            i.split_cost()

        print('\n每两人总花费:{}'.format(p_s.cost))

        self.assertTrue(item_1)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
