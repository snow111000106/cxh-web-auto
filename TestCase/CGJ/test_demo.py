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
        self.browser_cgj = PageObj(self.browser_driver).go_to_cgj_home()
        self.browser_cgj.login(mobile='14400000001', code='888888')
        time.sleep(3)
        self.browser_cgj.init()
        time.sleep(1)

    def teardown_class(self):
        self.browser_cgj.quit()

    @allure.story("test")
    def test_cgj(self):

        canvas = self.browser_cgj.get_canvas_info()
        script = "var rect = arguments[0].getBoundingClientRect(); return [rect.left, rect.top];"
        coords = self.browser_cgj.execute_script(script, canvas)
        print("Canvas坐标：", coords)

        # bro = self.browser_driver = init_driver()
        # bro.get('https://changkong-test.cds8.cn/home')
        # bro.find_element(By.XPATH, "//input[@placeholder='请输入手机号'and@class='el-input__inner']").send_keys('14400000001')
        # bro.find_element(By.XPATH, "//input[@placeholder='请输入验证码']").send_keys('888888')
        # bro.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[1]/div/div[2]/div[3]/button').click()
        # time.sleep(3)
        # bro.refresh()
        # time.sleep(2)
        # bro.refresh()
        # time.sleep(2)
        # html = bro.page_source
        # soup = BeautifulSoup(html, 'lxml')
        # canvas = soup.find_all('canvas')
        # print(canvas)
        # bro.quit()
