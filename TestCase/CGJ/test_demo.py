# -*- coding: utf-8 -*-
# @Time    : 2023/03/07
# @Author  : chenxuehong
# @File    : test_one_click_login.py

import time
from bs4 import BeautifulSoup
import allure
from Page.pageObj import PageObj
from WebBase.driver import init_driver


@allure.feature('测试蝉管家')
class TestCGJhome:

    def setup_class(self):
        self.browser_driver = init_driver()
        self.browser_cgj = PageObj(self.browser_driver).g()
        self.browser_cgj.login(mobile='14400000001', code='888888')
        time.sleep(3)
        self.browser_cgj.init()
        time.sleep(1)

    def teardown_class(self):
        self.browser_cgj.close()

    @allure.story("test")
    def test_cgj(self):

        canvas = self.browser_cgj.get_canvas_info()
        script = "var rect = arguments[0].getBoundingClientRect(); return [rect.left, rect.top];"
        coords = self.execute_script(script, canvas)
        print("Canvas坐标：", coords)
