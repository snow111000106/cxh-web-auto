# -*- coding: utf-8 -*-
# @Time    : 2023/07/29
# @Author  : chenxuehong
# @File    : cgj_login_page.py

import time
from WebBase.basepage import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class CgjHomePage(BasePage):
    # 蝉管家主页页面

    # 登陆入口
    login_enter = (By.XPATH, '//*[@id="app"]/div[1]/header/div[2]/div/button[2]')
    # 手机号输入框
    mobile_input = (By.XPATH, "//input[@placeholder='请输入手机号'and@class='el-input__inner']")
    # 验证码输入框
    code_input = (By.XPATH, "//input[@placeholder='请输入验证码']")
    # 登录按钮
    login_button = (By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[1]/div/div[2]/div[3]/button')
    # 我知道了按钮
    iknow_btn = (By.XPATH, '//*[@id="driver-popover-item"]/div[4]/button')
    # canvas画布
    canvas_class = (By.TAG_NAME, 'canvas')

    def __init__(self, driver):
        BasePage.__init__(self, driver)  # Base类的初始化

    def into_login_pop(self):
        """打开登陆窗口"""
        self.findElement(self.login_enter).click()
        return self

    def init(self):
        """初始化"""
        self.refresh(2)
        if self.isElemExist(self.iknow_btn):
            self.findElement(self.iknow_btn).click()

    def login(self, mobile, code):
        """登陆"""
        try:
            self.into_login_pop()
            self.findElement(self.mobile_input).send_keys(mobile)
            self.findElement(self.code_input).send_keys(code)
            self.findElement(self.login_button).click()
        except:
            print('账号登录失败')

    def get_canvas_info(self):
        canvas = self.findElement(self.canvas_class)
        return canvas











