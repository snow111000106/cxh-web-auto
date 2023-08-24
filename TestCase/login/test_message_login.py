# -*- coding: utf-8 -*-
# @Time    : 2023/03/13
# @Author  : chenxuehong
# @File    : test_message_login.py
import time

import allure
import pytest
from Config.config import Config
from Config.consts import CODE
from Page.pageObj import PageObj
from WebBase.driver import init_driver


@allure.feature('验证短信登录')
class TestMessageLogin:

    def setup_class(self):
        self.browser_driver = init_driver()
        self.browser = PageObj(self.browser_driver).go_to_login()
        self.browser.switch_login_type(types='register')
        time.sleep(2)

    def teardown_class(self):
        self.browser.close()

    @pytest.mark.tryfirst
    @allure.story("未输入手机号，获取验证码按钮/登录按钮置灰")
    def test_mobile_is_empty(self):

        self.browser.input_text(string=CODE, input_type='code')
        login_status = self.browser.get_btn_status(btn_name='login_button')
        code_status = self.browser.get_btn_status(btn_name='code_button_disable')
        assert not login_status
        assert not code_status

    @allure.story("未输入验证码，登录按钮置灰")
    def test_code_is_empty(self):

        self.browser.del_input()
        self.browser.input_text(string=Config.get_account_info(account=1), input_type='account')
        status = self.browser.get_btn_status(btn_name='login_button')
        assert not status

    @allure.story("输入手机号，获取验证码按钮高亮")
    def test_code_btn_status(self):

        self.browser.input_text(string=Config.get_account_info(account=1), input_type='account')
        status = self.browser.get_btn_status(btn_name='code_button_disable')
        assert status is True

    @allure.story("点击获取验证码弹出安全验证")
    def test_identification_pop(self):

        self.browser.input_text(string=Config.get_account_info(account=1), input_type='account')
        self.browser.click_element(element_name='code_button')
        status = self.browser.element_isExist(ele_name='safety_certification')
        self.browser.click_element(element_name='close_safety_cer')
        assert status is True

    @allure.story("输入错误的验证码，登录失败有提示")
    def test_code_is_error(self):

        self.browser.input_text(string=Config.get_account_info(account=1), input_type='account')
        self.browser.input_text(string='111111', input_type='code')
        self.browser.click_element(element_name='login_button')
        msg = self.browser.get_error_msg()
        assert msg == '认证失败'

    @allure.story("输入正确的账号/验证码（888888），可正常登录")
    def test_msg_login_normal(self):

        self.browser.input_text(string=Config.get_account_info(account=1), input_type='account')
        self.browser.input_text(string=CODE, input_type='code')
        status = self.browser.get_btn_status(btn_name='login_button')
        self.browser.click_element(element_name='login_button')
        result = self.browser.element_isExist(ele_name='user_picture')
        assert status is True
        assert result is True