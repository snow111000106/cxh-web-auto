# -*- coding: utf-8 -*-
# @Time    : 2023/07/29
# @Author  : chenxuehong
# @File    : cgj_big_home_page.py

import time
from WebBase.basepage import BasePage
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class CgjBigHomePage(BasePage):
    # 蝉管家大首页页面

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
    canvas_class = (By.XPATH, '//canvas')
    # 关闭活动弹窗
    close_pop_activity = (By.XPATH, '//*[@id="app"]/div[13]/div/div/div[2]/div/div[1]/div/div[2]/div/div')
    # 关闭更新弹窗
    close_pop_update = (By.XPATH, '//*[@id="app"]/div[13]/div/div/div[3]/div[1]/div/div[2]/div/div[1]/div/svg/path')
    # 折线图
    line_chart_ele = (By.XPATH, "//*[@id='sidebarInnerContent']/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/"
                                "div/div/div[2]")
    # 上一级ele
    up_ele = (By.XPATH, '//*[@id="sidebarInnerContent"]/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/'
                        'div/div/div[1]')

    def __init__(self, driver):
        BasePage.__init__(self, driver)  # Base类的初始化

    def into_login_pop(self):
        """打开登陆窗口"""
        self.findElement(self.login_enter).click()
        return self

    def init(self):
        """初始化"""
        try:
            self.refresh(times=2)
            if self.isElemExist(self.iknow_btn):
                self.findElement(self.iknow_btn).click()
            time.sleep(2)
        except Exception as e:
            print(e)

        return self

    def login(self, mobile, code):
        """登陆"""
        try:
            self.into_login_pop()
            self.findElement(self.mobile_input).send_keys(mobile)
            self.findElement(self.code_input).send_keys(code)
            self.findElement(self.login_button).click()
        except:
            print('账号登录失败')

    def get_line_chart_info(self, pix):

        webdriver.ActionChains(self).move_to_element(self.canvas_class).perform()
        time.sleep(2)
        div_ele = self.findElement(self.line_chart_ele)
        time.sleep(1)
        style_attribute = div_ele.get_attribute('style')
        print(style_attribute)
        left_value = int(style_attribute.split("left:")[1].split("px")[0].strip())
        new_left_value = left_value + pix
        self.execute_script("arguments[0].style.left = arguments[1] + 'px';", div_ele, new_left_value)
        time.sleep(2)
        next_level_element = div_ele.findElement(By.XPATH, "./div[1]")
        next_level_content = next_level_element.text
        return next_level_content











