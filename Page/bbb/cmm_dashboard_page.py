# -*- coding: utf-8 -*-
# @Time    : 2023/08/23
# @Author  : chenxuehong
# @File    : cmm_dashboard_page.py

import time
from WebBase.basepage import BasePage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class CmmDashBoardPage(BasePage):

    # 手机号输入框
    mobile_input = (By.XPATH, "//input[@placeholder='请输入手机号'and@class='el-input__inner']")

    def __init__(self, driver):
        BasePage.__init__(self, driver)  # Base类的初始化

    def click_logout_button(self):
        pass








