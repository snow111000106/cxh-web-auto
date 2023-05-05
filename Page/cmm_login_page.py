# -*- coding: utf-8 -*-
# @Time    : 2022/11/16
# @Author  : chenxuehong
# @File    : login_page.py

import time
from WebBase.basepage import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class CMMLoginPage(BasePage):
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

    def __init__(self, driver):
        BasePage.__init__(self, driver)  # Base类的初始化

    # 获取登出按钮
    def click_logout_button(self):
        menu = self.findElements(self.avatar)
        time.sleep(2)
        ActionChains(self.driver).move_to_element(menu[1]).perform()
        time.sleep(1)
        self.findElement(self.logout_button).click()

    def login(self, mobile, pwd):
        try:
            self.findElement(self.mobile_input).send_keys(mobile)
            self.findElement(self.pwd_input).send_keys(pwd)
            self.findElement(self.login_button).click()
        except:
            print('账号登录失败')








