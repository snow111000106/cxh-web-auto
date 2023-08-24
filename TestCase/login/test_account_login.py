# -*- coding: utf-8 -*-
# @Time    : 2023/03/07
# @Author  : chenxuehong
# @File    : test_account_login.py

import time
import allure
from Page.pageObj import PageObj
from Config.config import Config
from WebBase.driver import init_driver


@allure.feature('验证账号登录')
class TestAccountLogin:
    
    def setup_class(self):
        self.browser_driver = init_driver()
        self.browser = PageObj(self.browser_driver).go_to_login()
        
    def teardown_class(self):
        self.browser.close()

    @allure.story("未输入密码，登录按钮置灰")
    def test_pwd_is_empty(self):

        self.browser.input_text(string=Config.get_account_info(account=1), input_type='account')
        status = self.browser.get_btn_status(btn_name='login_button')
        self.browser.del_input()
        assert not status

    @allure.story("未输入账号，登录按钮置灰")
    def test_account_is_empty(self):

        self.browser.input_text(string=Config.get_account_info(pwd=1), input_type='password')
        status = self.browser.get_btn_status(btn_name='login_button')
        assert not status

    @allure.story("输入错误的账号，登录失败有提示")
    def test_account_is_error(self):

        self.browser.input_text(string='11111', input_type='account')
        self.browser.input_text(Config.get_account_info(pwd=1), input_type='password')
        self.browser.click_element(element_name='login_button')
        msg = self.browser.get_error_msg()
        assert msg == '手机号码格式有误'

    @allure.story("输入错误的密码，登录失败有提示")
    def test_pwd_is_error(self):

        self.browser.input_text(string=Config.get_account_info(account=1), input_type='account')
        self.browser.input_text(string='000000', input_type='password')
        self.browser.click_element(element_name='login_button')
        msg = self.browser.get_error_msg()
        assert msg == '账号或密码错误'

    @allure.story("输入正确的账号/密码，可正常登录")
    def test_pwd_login_normal(self):

        self.browser.input_text(string=Config.get_account_info(account=1), input_type='account')
        self.browser.input_text(string=Config.get_account_info(pwd=1), input_type='password')
        status = self.browser.get_btn_status(btn_name='login_button')
        self.browser.click_element(element_name='login_button')
        result = self.browser.element_isExist(ele_name='user_picture')
        assert status is True
        assert result is True
