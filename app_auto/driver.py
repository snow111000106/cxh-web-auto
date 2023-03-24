# -*- coding: utf-8 -*-
# @Time    : 2022/11/15
# @Author  : chenxuehong
# @File    : driver.py

from Config import devicesInfo
from selenium import webdriver
from Config.consts import path, deviceName, PLATFORM
import time



TIMEOUT = 10
POLL_FREQUENCY = 0.5


class Driver:

    driver = None

    @classmethod
    def get_driver(cls):
        if PLATFORM == 'web':
            if cls.driver is None:
                if deviceName == 'Chrome':
                    cls.driver = webdriver.Chrome()
                    cls.driver.maximize_window()
                elif deviceName == 'Firefox':
                    cls.driver = webdriver.Firefox()
                    cls.driver.maximize_window()
                else:
                    raise NameError(
                        "Not found %s browser,You can enter 'Chrome', 'Firefox'" % deviceName)
        elif PLATFORM == 'app':
            if cls.driver is None:
                des = devicesInfo.get_devices()
                cls.driver = webdriver.Remote(path, desired_capabilities=des)

                time.sleep(3)
            else:
                raise NameError("设备已启动")
        else:
            print('PLATFORM输入错误')

        return cls.driver

    # @classmethod
    # def quit_driver(cls):
    #
    #     if cls.driver:
    #         cls.driver.quit()
    #         cls.driver = None
