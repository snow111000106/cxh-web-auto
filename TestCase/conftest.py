# -*- coding: utf-8 -*-
# @Time    : 2022/11/17
# @Author  : chenxuehong
# @File    : conftest.py

import time
import os
from Common.base import Base


def pytest_terminal_summary(terminalreporter):

    """
    :param terminalreporter:
    :return:
    """

    _PASSED = len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
    _ERROR = len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
    _FAILED = len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
    _SKIPPED = len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])
    _TOTAL = terminalreporter._numcollected
    _TIMES = round(time.time() - terminalreporter._sessionstarttime, 2)
    times = Base.second_switch(_TIMES)

    send_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(send_time, _TOTAL, _PASSED, _FAILED, _SKIPPED, _ERROR, times)
    os.environ["REPORT"] = "自动化运行情况：\n发送时间: {},\n用例总数: {},\n通过用例数: {},\n失败用例数: {},\n跳过用例数: {},\n错误用例数: {},\n总用时: {}".format(send_time, _TOTAL, _PASSED, _FAILED, _SKIPPED, _ERROR, times)
