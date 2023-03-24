# -*- coding: utf-8 -*-
# @Time    : 2022/11/15
# @Author  : chenxuehong
# @File    : driver.py


from selenium import webdriver
from Config.consts import deviceName


def init_driver():

    if deviceName == 'Chrome':
        driver = webdriver.Chrome()

        return driver

    elif deviceName == 'Firefox':
        driver = webdriver.Firefox()

        return driver
    else:
        raise NameError(
            "Not found %s browser,You can enter 'Chrome', 'Firefox'" % deviceName)
