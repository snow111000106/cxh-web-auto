# -*- coding: utf-8 -*-
# @Time    : 2022/11/16
# @Author  : chenxuehong
# @File    : pageObj.py

from WebBase.basepage import BasePage
from Common.read_data import ReadYaml
from Page.login_page import LoginPage
from Page.home_page import HomePage
from Page.cmm_login_page import CMMLoginPage
from Page.cgj_home_page import CgjHomePage
from Page.authorLib_page import AuthorLibPage
from selenium.webdriver.common.by import By

web = ReadYaml.read_yaml_data(file_path='./Config/web.yaml')


class PageObj(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.find_author = (By.CSS_SELECTOR, 'a.menu-main.flex.align-items-center.text-decoration-none.author')

    def go_to_login(self):
        """
        跳转到蝉小红登录页
        :return:
        """
        try:
            self.openUrl(self.host + web['path']['login'])
            return LoginPage(self.driver)
        except:
            print('进入蝉小红登录页失败')

    def go_to_cmm_login(self):
        """
        跳转到蝉妈妈登录页
        :return:
        """
        try:
            self.openUrl('https://sv-test.cds8.cn/login')
            return CMMLoginPage(self.driver)
        except:
            print('进入蝉妈妈登录页失败')

    def go_to_cgj_home(self):
        """
        跳转到蝉管家主页
        :return:
        """
        try:
            self.openUrl('https://changkong-test.cds8.cn')
            return CgjHomePage(self.driver)
        except:
            print('进入蝉管家主页失败')

    def go_to_home(self):
        """
        跳转到蝉小红主页
        :return:
        """
        try:
            self.openUrl(self.host)
            return HomePage(self.driver)
        except:
            print('进入蝉小红主页失败')

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

