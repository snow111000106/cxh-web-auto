# -*- coding: utf-8 -*-
# @Time    : 2023/03/07
# @Author  : chenxuehong
# @File    : test_one_click_login.py
import time

import allure
from Page.pageObj import PageObj
from WebBase.driver import init_driver


@allure.feature('验证一键登录')
class TestOneClickLogin:

    def setup_class(self):
        self.browser_driver = init_driver()
        self.browser = PageObj(self.browser_driver).go_to_login()
        handle = self.browser.getWindowsHandle()
        print(handle)
        # self.browser.new_cmm_windows()
        # time.sleep(1)
        # self.browser.switchTag(handle[1])
        # # self.browser.login(username='13100000001', pwd='111111')

    # def teardown_class(self):
    #     self.browser.close()

    @allure.story("蝉妈妈登录账号，蝉小红自动获取蝉妈妈登录的账号")
    def test_get_cmm_account(self):

        self.browser.refresh(times=1)
