# -*- coding: utf-8 -*-
# @Time    : 2023/03/07
# @Author  : chenxuehong
# @File    : test_one_click_login.py

import time

import pytest
from selenium import webdriver
import allure
from WebBase.driver import init_driver
from Page.pageObj import PageObj


@allure.feature('蝉管家主页')
class TestCGJhome:

    def setup_class(self):
        self.browser_driver = init_driver()
        self.browser_cgj = PageObj(self.browser_driver).go_to_cgj_home()
        self.browser_cgj.login(mobile='14400000001', code='888888')
        time.sleep(10)
        # self.browser_cgj.init()

    def teardown_class(self):
        self.browser_cgj.quit()

    @allure.story("test")
    def test_cgj(self):
        for i in range(3):
            times = self.browser_cgj.get_line_chart_info(pix=(i+1)*100)
            print(times)