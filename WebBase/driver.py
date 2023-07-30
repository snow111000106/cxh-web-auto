# -*- coding: utf-8 -*-
# @Time    : 2022/11/15
# @Author  : chenxuehong
# @File    : driver.py


from selenium import webdriver
from Config.consts import deviceName


def init_driver():

    if deviceName == 'Chrome':
        option = webdriver.ChromeOptions()

        option.add_argument('--disable-blink-features=AutomationControlled')  # 禁用自动化检测
        option.add_argument("--disable-gpu")  # 禁用gpu渲染
        option.add_argument('--blink-settings=imagesEnabled=true')  # 显示图片

        # option.add_argument("--no-sandbox")  # 以最高权限运行
        # option.add_experimental_option('excludeSwitches', ['enable-automation'])  # 屏蔽受控提示
        # option.add_argument("user-agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36
        # (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'")  # 设置user-agent
        # option.add_argument('--auto-open-devtools-for-tabs')  # 开启开发者模式
        # option.add_argument('--headless')  # 无界面模式
        # option.add_argument("--disable-javascript")  # 禁用java脚本

        driver = webdriver.Chrome(options=option)

        return driver

    elif deviceName == 'Firefox':
        driver = webdriver.Firefox()
        return driver

    elif deviceName == 'Safari':
        driver = webdriver.Safari()

        return driver
    else:
        raise NameError(
            "Not found %s browser,You can enter 'Chrome', 'Firefox'" % deviceName)
