# -*- coding: utf-8 -*-
# @Time    : 2022/11/15
# @Author  : chenxuehong
# @File    : Consts.py

"""
全局变量
"""
# 环境test/stage/release
environment = 'test'
# 配置设备名称
deviceName = 'Chrome'  # 输入浏览器,Chrome/Firefox
# 远程路径
remote_path = 'http://127.0.0.1:4723'

default_account = {
    "test": 14400000001,
    "stage": 10002240004,
    "release": 10002240004
}
com_account = {
    "test": 14400000002,
    "stage": 15659809965,
    "release": 15659809965
}
per_account = {
    "test": 14400000003,
    "stage": 10002240002,
    "release": 10002240002
}
maj_account = {
    "test": 14400000004,
    "stage": 10002240003,
    "release": 10002240003
}
password = {
    "test": 123456,
    "stage": 123456,
    "release": 123456
}

# 钉钉机器人配置
webhook = \
    "https://oapi.dingtalk.com/robot/send?access_token=58a6c1f46c9fd95abb22ea63ee84531736fcd19f380ee9bb74e36be6480217a0"
secret = 'SECfe2c4dc43af5bd240e3db51d69192ffaddbba6dff8b42d2fe91b7ee9474764df'
at_phone = ["15659809965"]