# -*- coding: utf-8 -*-
# @Time    : 2022/11/16
# @Author  : chenxuehong
# @File    : authorLib_page.py

from WebBase.basepage import BasePage
from selenium.webdriver.common.by import By
import time


class AuthorLibPage(BasePage):
    # 蝉小红博主库页面

    # 获取用户vip等级
    vip_name = (By.CSS_SELECTOR, "span.c333.ml5")

    def __init__(self, driver):
        BasePage.__init__(self, driver)  # Base类的初始化

    def init(self):
        self.refresh(times=2)

    def get_vip(self):
        return self.findElement(self.vip_name).text

