# -*- coding: utf-8 -*-
# @Time    : 2022/11/15
# @Author  : chenxuehong
# @File    : driver.py

from Common.mylog import Mylog
from Config.config import Config
from selenium.webdriver.support.ui import WebDriverWait
import time


class BasePage(object):
    # 初始化
    # 建议格式AaaBbbCcc
    def __init__(self, deiver):
        # 获取主页地址
        self.host = Config.get_url()
        # 创建浏览器对象
        self.driver = deiver
        # 设置隐式等待
        self.driver.implicitly_wait(3)
        # 设置浏览器的最大化
        self.driver.maximize_window()

    def openUrl(self, url):
        try:
            self.driver.get(url)
            time.sleep(1)
        except:
            print('获取url失败，url为{}'.format(url))
            Mylog.error('获取url失败，url为{}'.format(url))

    def findElement(self, locator):
        wait = WebDriverWait(self.driver, 5, 0.5)
        element = wait.until(lambda x: x.find_element(*locator))
        return element

    def close(self):
        # 退出浏览器
        self.driver.close()

    def refresh(self, times):
        # 刷新页面
        for i in range(times):
            time.sleep(1)
            self.driver.refresh()

    def getCurrentUrl(self):
        try:
            url = self.driver.current_url()
            return url
        except:
            print('获取当前页面url失败')

    def isElemExist(self, elm):
        try:
            time.sleep(1)
            ele = self.findElement(elm)
            if ele:
                return True
        except Exception as e:
            return False

    def switchIframe(self, iframe):
        try:
            self.driver.switch_to.frame(iframe)
            time.sleep(2)
        except:
            print('切换iframe失败')

    def closeIframe(self):
        try:
            self.driver.switch_to.default_content()
        except:
            print('切换html失败')


if __name__ == '__main__':
    pass