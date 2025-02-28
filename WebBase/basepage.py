# -*- coding: utf-8 -*-
# @Time    : 2022/11/15
# @Author  : chenxuehong
# @File    : basepage.py

from Common.mylog import Mylog
from Config.config import Config
from selenium.webdriver.support.ui import WebDriverWait
import time


class BasePage(object):
    # 初始化
    # 建议格式AaaBbbCcc
    def __init__(self, driver):

        self.host = Config.get_url(types='aaa')
        self.cmm_host = Config.get_url(types='bbb')
        self.cgj_host = Config.get_url(types='ccc')
        # 创建浏览器对象
        self.driver = driver
        # 设置隐式等待
        self.driver.implicitly_wait(3)
        # 设置浏览器的最大化
        self.driver.maximize_window()

    def openUrl(self, url):
        """打开url"""
        try:
            self.driver.get(url)
            time.sleep(1)
        except:
            print('获取url失败，url为{}'.format(url))
            Mylog.error('获取url失败，url为{}'.format(url))

    def findElement(self, locator, timeout=5, poll_frequency=0.5):
        """定位元素"""
        wait = WebDriverWait(self.driver, timeout, poll_frequency)
        element = wait.until(lambda x: x.find_element(*locator))
        return element

    def findElements(self, locator):
        """定位多个元素"""
        elements = self.driver.find_elements(*locator)
        return elements

    def close(self):
        """关闭浏览器"""
        self.driver.close()

    def quit(self):
        """退出浏览器"""
        self.driver.quit()

    def refresh(self, times, du=1):
        """刷新页面"""
        for i in range(times):
            time.sleep(du)
            self.driver.refresh()

    def clear_cookie(self):
        """清除缓存"""
        self.driver.delete_all_cookies()

    def getCurrentUrl(self):
        """获取当前页面url"""
        try:
            url = self.driver.current_url()
            return url
        except:
            print('获取当前页面url失败')

    def isElemExist(self, elm):
        """判断元素是否存在"""
        try:
            time.sleep(1)
            ele = self.findElement(elm)
            if ele:
                return True
        except Exception as e:
            return False

    def switchIframe(self, iframe):
        """切换至iframe"""
        try:
            self.driver.switch_to.frame(iframe)
            time.sleep(2)
        except:
            print('切换iframe失败')

    def closeIframe(self):
        """关闭iframe"""
        try:
            self.driver.switch_to.default_content()
        except:
            print('切换html失败')

    def newTag(self, tab_name):
        """新建一个窗口"""
        try:
            self.driver.switch_to.new_window(tab_name)
        except:
            print('新建窗口失败')

    def switchTag(self, handles):
        """切换到不同的窗口"""
        try:
            self.driver.switch_to.window(handles)
        except:
            print('切换窗口失败')

    def execute_script(self, script, *args):
        """插入脚本"""
        return self.driver.execute_script(script, *args)

    def getWindowsHandle(self, types='current'):
        """获取当前窗口handle"""
        try:
            tag = None
            if types == 'all':
                tag = self.driver.window_handles
            if types == 'current':
                tag = self.driver.current_window_handle
            return tag
        except:
            print('获取窗口标签失败')

    def back(self):
        """返回上一级"""
        try:
            self.driver.back()
        except:
            print('回退失败')

    def forward(self):
        """前进一级"""
        try:
            self.driver.forward()
        except:
            print('前进失败')


if __name__ == '__main__':
    pass