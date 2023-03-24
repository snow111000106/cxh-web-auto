# -*- coding: utf-8 -*-
# @Time    : 2022/11/17
# @Author  : chenxuehong
# @File    : test_home.py

from WebBase.driver import init_driver
from Page.pageObj import PageObj
import allure


class TestAuthorLib:

    def setup_method(self):
        self.driver = init_driver()

    def teardown_method(self):
        self.driver.quit()

    @allure.story("验证会员1")
    def test_author_home(self):
        vip_name = PageObj(self.driver).go_to_authorLib().get_vip()
        assert vip_name == '企业版'

    @allure.story("验证会员2")
    def test_author_home_2(self):
        vip_name = PageObj(self.driver).go_to_authorLib().get_vip()
        assert vip_name == '专业版'
