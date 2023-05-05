# -*- coding: utf-8 -*-
# @Time    : 2022/11/17
# @Author  : chenxuehong
# @File    : test_home.py

from WebBase.driver import init_driver
from Page.pageObj import PageObj
import allure


class TestAuthorLib:

    @allure.story("验证会员1")
    def test_author_home(self, go_to_login):
        self.bro = go_to_login
        self.vip = self.bro.get_vip()
        assert self.vip == '企业版'

    @allure.story("验证会员2")
    def test_author_home_2(self, go_to_login):
        self.bro = go_to_login
        self.vip = self.bro.get_vip()
        assert self.vip == '企业版'
