# -*- coding: utf-8 -*-
# @Time    : 2023/03/07
# @Author  : chenxuehong
# @File    : test_one_click_login.py
import time
from Config.config import Config
import allure
from Page.pageObj import PageObj
from WebBase.driver import init_driver


@allure.feature('验证一键登录')
class TestOneClickLogin:

    def setup_class(self):

        self.browser_driver = init_driver()
        self.browser_cxh = PageObj(self.browser_driver).go_to_login()
        time.sleep(2)
        self.cxh_handle = self.browser_cxh.getWindowsHandle()

        self.browser_cxh.new_cmm_windows()
        self.browser_cmm = PageObj(self.browser_driver).go_to_cmm_login()
        self.browser_cmm.login(mobile=Config.get_account_info(account=1), pwd=Config.get_account_info(pwd=1))
        time.sleep(2)
        self.cmm_handle = self.browser_cmm.getWindowsHandle()
        self.browser_cmm.switchTag(self.cxh_handle)
        time.sleep(2)

    def teardown_class(self):
        self.browser_cmm.quit()
        self.browser_cxh.quit()

    @allure.story("蝉妈妈登录账号，蝉小红自动获取蝉妈妈登录的账号")
    def test_get_cmm_account(self):

        self.browser_cxh.refresh(times=2)
        status = self.browser_cxh.element_isExist(ele_name='el_login_button')
        assert status is True

    @allure.story("蝉妈妈登录账号，蝉小红可切换使用其他账号登录")
    def test_switch_account_login(self):

        self.browser_cxh.click_element(element_name='other_login_btn')
        status = self.browser_cxh.element_isExist(ele_name='username_input')
        assert status is True

    @allure.story("蝉妈妈登录账号，蝉小红可一键登录")
    def test_cxh_el_login(self):

        self.browser_cxh.refresh(times=2)
        self.browser_cxh.click_element(element_name='el_login_button')
        status = self.browser_cxh.element_isExist(ele_name='user_picture')
        assert status is True

    @allure.story("蝉妈妈退出账号，蝉小红不会退出账号")
    def test_logout_cmm_account(self):

        self.browser_cxh.switchTag(self.cmm_handle)
        self.browser_cmm.click_logout_button()
        self.browser_cmm.clear_cookie()  # 清除缓存
        self.browser_cmm.switchTag(self.cxh_handle)
        self.browser_cxh.refresh(times=2)
        status = self.browser_cxh.element_isExist(ele_name='user_picture')
        assert status is True

    @allure.story("蝉妈妈退出登录后，蝉小红退出账号，蝉小红不会出现一键登录")
    def test_logout_cxh_account(self):

        self.browser_cxh.refresh(times=3, du=2)
        self.browser_cxh.click_logout_button()
        self.browser_cxh.refresh(times=1)
        status = self.browser_cxh.element_isExist(ele_name='el_login_button')
        assert status is False
