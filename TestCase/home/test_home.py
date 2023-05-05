# -*- coding: utf-8 -*-
# @Time    : 2022/11/17
# @Author  : chenxuehong
# @File    : test_home.py

from Page.pageObj import PageObj
import allure


class TestHome:

    @allure.story("验证会员版本")
    def test_cxh_vip(self, go_to_login):
        self.bro = go_to_login
        self.vip = self.bro.get_vip()
        assert self.vip == '企业版'

    @allure.story("验证会员版本2")
    def test_cxh_home_2(self, go_to_login):
        self.bro = go_to_login
        self.vip = self.bro.get_vip()
        assert self.vip == '专业版'


