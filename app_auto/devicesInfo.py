# -*- coding: utf-8 -*-
# @Time    : 2022/11/15
# @Author  : chenxuehong
# @File    : devicesInfo.py

import yaml
from Config.consts import deviceName
from Common.mylog import Mylog

"""
设备信息
"""

with open('./Config/app.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)


def get_devices():
    desired = None

    if deviceName == "ios":
        # 苹果手机
        desired = {
            "platformName": "ios",
            "appium:platformVersion": "15.4.1",
            "appium:deviceName": "虹",
            "appium:automationName": "XCUITest",
            "appium:noReset": True,
            "appium:bundleId": "com.tencent.xin",
            "appium:webDriverAgentUrl": "http://localhost:8100",
            "appium:usePrebuiltWDA": True,
            "appium:useXctestrunFile": False,
            "appium:udid": "00008101-001E554C0178001E"
        }
    elif deviceName == "android":
        # 华为手机
        desired = {
            "platformName": "Android",
            "appium:platformVersion": "9",
            "appium:deviceName": "37KNW18802000695",
            "appium:noReset": True,
            "appium:appPackage": "com.chandashi.chanmama",
            "appium:automationName": "UiAutomator2",
            "appium:appActivity": ".operation.home.activity.LauncherActivity",
            "appium:ignoreHiddenApiPolicyError": True,
            "appium:unicodeKeyboard": True,  # 设置编码格式为unicode
            "appium:resetKeyboard": True  # 隐藏手机键盘
        }
    elif deviceName == 'applets':
        # 华为手机小程序
        desired = {
            "platformName": "Android",
            "appium:platformVersion": "9",
            "appium:deviceName": "37KNW18802000695",
            "appium:noReset": True,
            "appium:automationName": "UiAutomator2",
            "appium:appPackage": "com.tencent.mm",
            "appium:appActivity": "com.tencent.mm.ui.LauncherUI",
            "appium:chromeOptions": {'androidProcess': 'com.android.browser'},
            "appium:unicodeKeyboard": True,  # 设置编码格式为unicode
            "appium:resetKeyboard": True  # 隐藏手机键盘
        }

    else:
        print("PLATFORM输入错误不存在")
        Mylog.error("设备名称不存在")

    return desired
