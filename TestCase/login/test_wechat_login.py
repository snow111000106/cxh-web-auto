# -*- coding: utf-8 -*-
# @Time    : 2023/03/07
# @Author  : chenxuehong
# @File    : test_wechat_login.py

import allure
from Page.pageObj import PageObj
from WebBase.driver import init_driver


@allure.feature('验证微信登录')
class TestWechatLogin:

    def setup_class(self):
        self.browser_driver = init_driver()
        self.browser = PageObj(self.browser_driver).go_to_login()

    def teardown_class(self):
        self.browser.close()

    @allure.story("点击微信登录，弹出扫码登录弹窗")
    def test_pwd_is_empty(self):

        self.browser.click_element(element_name='wechat_button')
        status = self.browser.element_isExist(ele_name='wechat_code')
        assert status is True