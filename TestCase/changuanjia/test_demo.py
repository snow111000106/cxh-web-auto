# -*- coding: utf-8 -*-
# @Time    : 2023/03/07
# @Author  : chenxuehong
# @File    : test_demo.py

import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import allure
from selenium.webdriver.common.by import By
from Page.pageObj import PageObj
from WebBase.driver import init_driver


@allure.feature('测试蝉管家')
class TestCGJhome:

    # def setup_class(self):
    #     self.browser_driver = init_driver()
    #     self.browser_cgj = PageObj(self.browser_driver).go_to_cgj_home()
    #     self.browser_cgj.login(mobile='14400000001', code='888888')
    #     time.sleep(3)
    #     self.browser_cgj.init()
    #     time.sleep(1)
    #
    # def teardown_class(self):
    #     self.browser_cgj.quit()

    @allure.story("test")
    def test_cgj(self):

        # canvas = self.browser_cgj.get_canvas_info()
        # action = webdriver.ActionChains(self.browser_cgj)
        # action.move_to_element(canvas).perform()
        # tooltip = self.browser_cgj.execute_script("return arguments[0].getAttribute('title');", canvas)
        # print("提示信息：", tooltip)

        # coords = self.browser_cgj.execute_script(
        #     "var rect = arguments[0].getBoundingClientRect(); return [rect.left, rect.top];", canvas)
        # canvas_width = self.browser_cgj.execute_script("return arguments[0].width", canvas)
        # canvas_height = self.browser_cgj.execute_script("return arguments[0].height", canvas)
        # print(coords, canvas_height, canvas_width)
        # script = "var rect = arguments[0].getBoundingClientRect(); return [rect.left, rect.top];"
        # coords = self.browser_cgj.execute_script(script, canvas)
        # print("Canvas坐标：", coords)

        bro = self.browser_driver = init_driver()
        bro.get('https://changkong-test.cds8.cn/home')
        bro.maximize_window()
        bro.find_element(By.XPATH, "//input[@placeholder='请输入手机号'and@class='el-input__inner']").send_keys('14400000001')
        bro.find_element(By.XPATH, "//input[@placeholder='请输入验证码']").send_keys('888888')
        bro.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/div[1]/div/div[2]/div[3]/button').click()
        time.sleep(3)
        bro.refresh()
        time.sleep(2)
        bro.refresh()
        time.sleep(2)
        canvas_element = bro.find_element(By.XPATH, "//*[@id='sidebarInnerContent']/div[1]/div/div[2]/div[1]/div[1]/"
                                                    "div[2]/div[1]/div[2]/div/div/div[1]")
        for i in range(10):

            webdriver.ActionChains(bro).move_to_element_with_offset(canvas_element, -10*i, 0).perform()
            time.sleep(2)
            div_ele = bro.find_element(By.XPATH, "//*[@id='sidebarInnerContent']/div[1]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/"
                                    "div/div/div[2]")
            time.sleep(1)
            times = div_ele.find_element(By.XPATH, "./div[1]")
            aa = div_ele.find_element(By.XPATH, './div[2]/div[1]/div/div/div/span[2]')
            ab = div_ele.find_element(By.XPATH, './div[2]/div[1]/div/div/span')
            ba = div_ele.find_element(By.XPATH, './div[2]/div[2]/div/div/div/span[2]')
            bb = div_ele.find_element(By.XPATH, './div[2]/div[2]/div/div/span')

            print(times.text, aa.text, ab.text, ba.text, bb.text)

        # style_attribute = div_ele.get_attribute('style')
        # print(style_attribute)
        # left_value = int(style_attribute.split("left:")[1].split("px")[0].strip())
        # new_left_value = left_value + 100
        # bro.execute_script("arguments[0].style.left = arguments[1] + 'px';", div_ele, new_left_value)
        # time.sleep(2)

        # actions = webdriver.ActionChains(bro)
        # actions.move_to_element_with_offset(canvas_element, 0, 0).perform()
        # canvas_width = bro.execute_script("return arguments[0].width", canvas_element)
        # canvas_height = bro.execute_script("return arguments[0].height", canvas_element)
        #
        # def get_tooltip_at_point(driver, x, y):
        #     script = f"var ctx = arguments[0].getContext('2d');" \
        #              f"var pixel = ctx.getImageData({x}, {y}, 1, 1);" \
        #              f"return pixel.data;"
        #     pixel_data = driver.execute_script(script, canvas_element)
        #     return pixel_data
        #
        # for x in range(0, canvas_width):
        #     for y in range(0, canvas_height):
        #         tooltip = get_tooltip_at_point(bro, x, y)
        #         if tooltip:
        #             print(f"点 ({x}, {y}) 的提示信息： {tooltip}")

        # html = bro.page_source
        # soup = BeautifulSoup(html, 'lxml')
        # canvas = soup.find_all('canvas')
        bro.quit()
