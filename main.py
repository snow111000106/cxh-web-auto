# -*- coding: utf-8 -*-
# @Time    : 2022/11/17
# @Author  : chenxuehong
# @File    : main.py

import pytest
import os


if __name__ == "__main__":

    args = ["./TestCase/home", "-s", "--alluredir=./Report/allure-results", "--clean-alluredir"]
    pytest.main(args)
    os.system(r"allure generate --clean ./Report/allure-results/ -o ./Report/html")
    os.system(r"allure serve ./Report/allure-results")