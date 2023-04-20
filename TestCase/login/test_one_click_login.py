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
        self.cxh_handle = self.browser.getWindowsHandle()
        self.browser.new_cmm_windows()
        self.browser_cmm = PageObj(self.browser_driver).go_to_cmm_login()
        self.cmm_handle = self.browser.getWindowsHandle()
        self.browser_cmm.login(mobile='13100000001', pwd='111111')
        self.browser_cmm.switchTag(self.cxh_handle)
        time.sleep(1)

    def teardown_class(self):
        self.browser.quit()

    @allure.story("蝉妈妈登录账号，蝉小红自动获取蝉妈妈登录的账号")
    def test_get_cmm_account(self):

        self.browser.refresh(times=2)
        status = self.browser.element_isExist(ele_name='el_login_button')
        assert status is True

    @allure.story("蝉妈妈登录账号，蝉小红可切换使用其他账号登录")
    def test_switch_account_login(self):

        self.browser.click_element(element_name='other_login_btn')
        status = self.browser.element_isExist(ele_name='username_input')
        assert status is True

    @allure.story("蝉妈妈登录账号，蝉小红可一键登录")
    def test_cxh_el_login(self):

        self.browser.refresh(times=2)
        self.browser.click_element(element_name='el_login_button')
        status = self.browser.element_isExist(ele_name='user_picture')
        assert status is True

    @allure.story("蝉妈妈退出账号，蝉小红不会退出账号")
    def test_logout_cmm_account(self):

        self.browser_cmm.switchTag(self.cmm_handle)
        self.browser_cmm.click_logout_button()
        self.browser_cmm.switchTag(self.cxh_handle)
        self.browser.refresh(times=2)
        status = self.browser.element_isExist(ele_name='user_picture')
        assert status is True

    @allure.story("蝉妈妈退出登录后，蝉小红退出账号，蝉小红不会出现一键登录")
    def test_logout_cxh_account(self):

        self.browser.click_logout_button()
        self.browser.refresh(times=2)
        status = self.browser.element_isExist(ele_name='el_login_button')
        assert status is False
