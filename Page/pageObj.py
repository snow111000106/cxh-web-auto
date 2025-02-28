# -*- coding: utf-8 -*-
# @Time    : 2022/11/16
# @Author  : chenxuehong
# @File    : pageObj.py

from WebBase.basepage import BasePage
from Common.read_data import ReadYaml
from Page.aaa.login_page import CxhLoginPage
from Page.aaa.home_page import CxhHomePage
from Page.aaa.authorLib_page import CxhAuthorLibPage
from Page.aaa.dashboard_page import CxhDashBoardPage
from Page.bbb.cmm_login_page import CmmLoginPage
from Page.bbb.cmm_big_home_page import CmmBigHomePage
from Page.bbb.cmm_dashboard_page import CmmDashBoardPage
from Page.ccc.cgj_big_home_page import CgjBigHomePage
from Page.ccc.cgj_home_page import CgjHomePage
from selenium.webdriver.common.by import By

web = ReadYaml.read_yaml_data(file_path='./Config/path.yaml')


class PageObj(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.find_author = (By.CSS_SELECTOR, 'a.menu-main.flex.align-items-center.text-decoration-none.author')

    def go_to_login(self):
        """
        跳转到aaa登录页
        :return:
        """
        try:
            self.openUrl(self.host + web['cxh_path']['login'])
            return CxhLoginPage(self.driver)
        except:
            print('进入aaa登录页失败')

    def go_to_home(self):
        """
        跳转到aaa主页
        :return:
        """
        try:
            self.openUrl(self.host)
            return CxhHomePage(self.driver)
        except:
            print('进入aaa主页失败')

    def switch_to_home(self):
        """
        切换到aaa主页
        :return:
        """
        try:
            return CxhHomePage(self.driver)
        except:
            print('进入aaa主页失败')

    def go_to_authorLib(self):
        """
        跳转到aaa我的博主库页面
        :return:
        """
        try:
            self.openUrl(self.host + web['cxh_path']['authorLib'])
            return CxhAuthorLibPage(self.driver)
        except:
            print('进入aaa博主库失败')

    def go_to_dashboard(self):
        """
        跳转到aaa数据看板页面
        :return:
        """
        try:
            self.openUrl(self.host + web['cxh_path']['dashboard'])
            return CxhDashBoardPage(self.driver)
        except:
            print('进入aaa博主库失败')

    def go_to_cmm_big_home(self):
        """
        跳转到bbb大首页
        :return:
        """
        try:
            self.openUrl(self.cmm_host)
            return CmmBigHomePage(self.driver)
        except:
            print('进入bbb大首页失败')

    def go_to_cmm_login(self):
        """
        跳转到bbb登录页
        :return:
        """
        try:
            self.openUrl(self.cmm_host + web['cmm_path']['login'])
            return CmmLoginPage(self.driver)
        except:
            print('进入bbb登录页失败')

    def go_to_cmm_dashboard(self):
        """
        跳转到bbb数据看板页面
        :return:
        """
        try:
            self.openUrl(self.cmm_host + web['cmm_path']['dashboard'])
            return CmmDashBoardPage(self.driver)
        except:
            print('进入bbb登录页失败')

    def go_to_cgj_big_home(self):
        """
        跳转到ccc大首页
        :return:
        """
        try:
            self.openUrl(self.cgj_host)
            return CgjBigHomePage(self.driver)
        except:
            print('进入ccc大首页失败')

    def go_to_cgj_home(self):
        """
        跳转到ccc首页
        :return:
        """
        try:
            self.openUrl(self.cgj_host + web['cgj_path']['home'])
            return CgjHomePage(self.driver)
        except:
            print('进入cc首页失败')



