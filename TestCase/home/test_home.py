# -*- coding: utf-8 -*-
# @Time    : 2022/11/17
# @Author  : chenxuehong
# @File    : test_home.py

from Page.pageObj import PageObj
import allure


class TestHome:

    @allure.story("验证会员版本1")
    def test_cxh_home(self, browser):
        vip_name = PageObj(browser).go_to_home().get_vip()
        assert vip_name == '企业版'

    @allure.story("验证会员版本2")
    def test_cxh_home_2(self, browser):
        vip_name = PageObj(browser).go_to_home().get_vip()
        assert vip_name == '专业版'


