# -*- coding: utf-8 -*-
# @Time    : 2022/11/16
# @Author  : chenxuehong
# @File    : cmm_login_page.py

import time
from WebBase.basepage import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class CmmLoginPage(BasePage):
    # 蝉妈妈登录页面

    # 手机号输入框
    mobile_input = (By.XPATH, "//input[@placeholder='请输入手机号'and@class='el-input__inner']")
    # 密码输入框
    pwd_input = (By.XPATH, "//input[@placeholder='请输入密码']")
    # 登录按钮
    login_button = (By.ID, "e2e-login-submit")
    # 登出按钮
    logout_button = (By.XPATH, "/html/body/div[3]/ul/li/ul/div[1]/div[3]")
    # 会员头像
    avatar = (By.CLASS_NAME, "el-submenu__title")
    # 注册/登录入口
    register_enter = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[1]/div[3]/div[2]')

    def __init__(self, driver):
        BasePage.__init__(self, driver)  # Base类的初始化

    def click_logout_button(self):
        menu = self.findElements(self.avatar)
        action = ActionChains(self.driver)
        action.move_to_element(menu[1]).perform()
        time.sleep(2)
        self.findElement(self.logout_button).click()
        time.sleep(1)

    def login(self, mobile, pwd):
        try:
            self.findElement(self.mobile_input).send_keys(mobile)
            self.findElement(self.pwd_input).send_keys(pwd)
            self.findElement(self.login_button).click()
        except:
            print('账号登录失败')

    def wait_for_ele(self, ele_name, timeout):
        """等待元素出现"""
        try:
            if ele_name == 'mobile_input':
                self.findElement(self.mobile_input, timeout=timeout)
            return True
        except Exception as e:
            print(e)







