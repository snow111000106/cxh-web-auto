# -*- coding: utf-8 -*-
# @Time    : 2022/11/16
# @Author  : chenxuehong
# @File    : login_page.py

import time
from WebBase.basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class LoginPage(BasePage):
    # 登录页面

    # 手机号输入框
    username_input = (By.XPATH, "//input[@placeholder='请输入手机号'and@class='el-input__inner']")
    # 密码输入框
    pwd_input = (By.XPATH, "//input[@placeholder='请输入密码']")
    # 验证码输入框
    verification_code_input = (By.XPATH, "//input[@placeholder='请输入验证码']")
    # 获取验证码按钮
    code_button = (By.CSS_SELECTOR, ".flex.align-items-center.justify-content-center.fs14")
    # 获取验证码按钮_disable
    code_button_disable = (By.CSS_SELECTOR, ".el-tooltip.get-code.item.disable")
    # 登录按钮
    login_button = (By.XPATH, '//button')
    # 清除输入手机号按钮
    clear_button = (By.CSS_SELECTOR, 'div.clear-icon')
    # 一键登录按钮
    el_login_button = (By.CSS_SELECTOR, 'button.el-button.login-btn')
    # 微信登录按钮
    wechat_button = (By.CSS_SELECTOR, 'i.cursor-pointer')
    # 忘记密码
    forgot_pwd = (By.CSS_SELECTOR, 'div.cp.cursor-pointer.fs12')
    # 短信登录/注册入口
    enter_register = (By.XPATH, "//li[@class='el-menu-item']")
    # 账号登录入口
    enter_login = (By.CSS_SELECTOR, 'li.el-menu-item.is-active')
    # 错误提示toast
    error_message = (By.XPATH, "//p[@class='el-message__content']")
    # 用户头像
    user_picture = (By.CLASS_NAME, 'img-bg')
    # 安全认证弹窗
    safety_certification = (By.XPATH, "//img[@class='img-back']")
    # 关闭安全认证弹窗
    close_safety_cer = (By.XPATH, "//img[@src='https://cdn-static.chanmama.com/sub-module/static-file/6/9/1e3f903b32']")
    # 定位iframe
    iframe = (By.XPATH, "//iframe[@src='https://captcha-service.chanmama.com?aid=CXH']")
    # 微信扫码登录弹窗
    wechat_code = (By.CLASS_NAME, 'code-logo')
    # 使用其他账号登录按钮
    other_login_btn = (By.CLASS_NAME, 'c333.fs1.ml5')
    # 登出按钮
    logout_button = (By.XPATH, "/html/body/div[3]/ul/li/ul/div[1]/div[3]")

    def __init__(self, driver):
        BasePage.__init__(self, driver)  # Base类的初始化

    def login_clear_input(self, input_type):
        try:
            if input_type == 'account':
                self.findElement(self.username_input).clear()
            if input_type == 'password':
                self.findElement(self.pwd_input).clear()
            if input_type == 'code':
                self.findElement(self.verification_code_input).clear()
        except:
            print('清除登录页面输入框异常')

    def del_input(self):
        try:
            self.findElement(self.clear_button).click()
        except:
            print('删除登录页面输入异常')

    def input_text(self, string, input_type):
        try:
            if input_type == 'account':
                self.findElement(self.username_input).clear()
                self.findElement(self.username_input).send_keys(string)
            if input_type == 'password':
                self.findElement(self.pwd_input).clear()
                self.findElement(self.pwd_input).send_keys(string)
            if input_type == 'code':
                self.findElement(self.verification_code_input).clear()
                self.findElement(self.verification_code_input).send_keys(string)
        except Exception as e:
            print(e)
        except:
            print('无法点击{}'.format(input_type))

    def click_element(self, element_name):
        try:
            if element_name == 'code_button':
                self.findElement(self.code_button).click()
            if element_name == 'wechat_button':
                self.findElement(self.wechat_button).click()
            if element_name == 'login_button':
                self.findElement(self.login_button).click()
            if element_name == 'other_login_btn':
                self.findElement(self.other_login_btn).click()
            if element_name == 'el_login_button':
                self.findElement(self.el_login_button).click()
            if element_name == 'close_safety_cer':
                self.switchIframe(self.findElement(self.iframe))
                time.sleep(1)
                self.findElement(self.close_safety_cer).click()
                self.closeIframe()
        except Exception as e:
            print(e)
        except:
            print('无法点击{}'.format(element_name))

    def get_btn_status(self, btn_name):
        try:
            status = None
            if btn_name == 'login_button':
                elm = self.findElement(self.login_button)
                status = elm.is_enabled()
            if btn_name == 'code_button_disable':
                elm = self.isElemExist(self.code_button_disable)
                if elm:
                    status = False
                else:
                    status = True
            return status
        except Exception as e:
            print(e)

    def get_error_msg(self):
        try:
            time.sleep(2)
            msg = self.findElement(self.error_message).text
            return msg
        except:
            print('获取错误提示失败')

    def element_isExist(self, ele_name):
        try:
            result = None
            if ele_name == 'user_picture':
                result = self.isElemExist(self.user_picture)
            if ele_name == 'safety_certification':
                self.switchIframe(self.findElement(self.iframe))
                time.sleep(1)
                result = self.isElemExist(self.safety_certification)
                self.closeIframe()
            if ele_name == 'wechat_code':
                result = self.isElemExist(self.wechat_code)
            if ele_name == 'el_login_button':
                result = self.isElemExist(self.el_login_button)
            if ele_name == 'username_input':
                result = self.isElemExist(self.username_input)
            return result
        except Exception as e:
            print(e)

    def switch_login_type(self, types):
        try:
            if types == 'login':
                self.findElement(self.enter_login).click()
            if types == 'register':
                self.findElement(self.enter_register).click()
        except:
            print('切换登录/注册失败')

    def login(self, username, pwd=None, types='password'):

        if types == 'password':
            try:
                self.switch_login_type(types='login')
                self.input_text(string=username, input_type='account')
                self.input_text(string=pwd, input_type='password')
                self.click_element(element_name='login_button')
            except:
                print('账号登录失败')
        if types == 'message' or types == 'register':
            try:
                self.switch_login_type(types='register')
                self.input_text(string=username, input_type='account')
                self.input_text(string='888888', input_type='code')
                self.click_element(element_name='login_button')
                time.sleep(1)
            except:
                print('短信登录/注册失败')

    def new_cmm_windows(self):
        self.newTag(tab_name='cmm')

    def click_logout_button(self):
        menu = self.findElement(self.user_picture)
        time.sleep(2)
        ActionChains(self.driver).move_to_element(menu).perform()
        time.sleep(2)
        self.findElement(self.logout_button).click()





