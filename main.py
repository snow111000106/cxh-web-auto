# -*- coding: utf-8 -*-
# @Time    : 2022/11/17
# @Author  : chenxuehong
# @File    : main.py

import pytest
import os
from Utils.dingTalkNotice import DingNotic


if __name__ == "__main__":

    args = ["./TestCase/CGJ", "-s", "--alluredir=./Report/allure-results", "--clean-alluredir"]
    pytest.main(args)
    # DingNotic.dingding_notice()
    os.system(r"allure generate --clean ./Report/allure-results/ -o ./Report/html")
    os.system(r"allure serve ./Report/allure-results")