# -*- coding: utf-8 -*-
# @Time    : 2022/11/16
# @Author  : chenxuehong
# @File    : login_page.py

import time
from WebBase.basepage import BasePage
from selenium.webdriver.common.by import By


class CMMLoginPage(BasePage):
    # 蝉妈妈登录页面

    # 手机号输入框
    mobile_input = (By.XPATH, "//input[@placeholder='请输入手机号'and@class='el-input__inner']")

    # 密码输入框
    pwd_input = (By.XPATH, "//input[@placeholder='请输入密码']")

    # 登录按钮
    login_button = (By.XPATH, "//button[@class='el-dialog__headerbtn']")

    def __init__(self, driver):
        BasePage.__init__(self, driver)  # Base类的初始化

    def login(self, mobile, pwd):
        try:
            self.findElement(self.mobile_input).send_keys(mobile)
            self.findElement(self.pwd_input).send_keys(pwd)
            self.findElement(self.login_button).click()
        except:
            print('账号登录失败')








