# -*- coding: utf-8 -*-
# @Time    : 2022/11/16
# @Author  : chenxuehong
# @File    : pageObj.py

from WebBase.basepage import BasePage
from Common.read_data import ReadYaml
from Page.login_page import LoginPage
from Page.home_page import HomePage
from Page.authorLib_page import AuthorLibPage
from selenium.webdriver.common.by import By

web = ReadYaml.read_yaml_data(file_path='./Config/web.yaml')


class PageObj(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.find_author = (By.CSS_SELECTOR, 'a.menu-main.flex.align-items-center.text-decoration-none.author')

    def go_to_login(self):
        """
        跳转到登录页
        :return:
        """
        try:
            self.openUrl(self.host + web['path']['login'])
            return LoginPage(self.driver)
        except:
            print('进入登录页失败')

    def go_to_home(self):
        """
        跳转到主页
        :return:
        """
        try:
            self.openUrl(self.host)
            return HomePage(self.driver)
        except:
            print('进入主页失败')

    def switch_to_home(self):
        """
        跳转到主页
        :return:
        """
        try:
            return HomePage(self.driver)
        except:
            print('进入主页失败')

    def go_to_authorLib(self):
        """
        跳转到我的博主搜索页
        :return:
        """
        try:
            self.openUrl(self.host + web['path']['authorLib'])
            return AuthorLibPage(self.driver)
        except:
            print('进入博主库失败')

