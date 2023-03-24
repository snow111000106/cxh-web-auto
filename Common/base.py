# -*- coding: utf-8 -*-
# @Time    : 2022/11/15
# @Author  : chenxuehong
# @File    : base.py

import time


class Base():

    @staticmethod
    def second_switch(second) -> str:

        """
            秒转换为时分秒
        """
        if second < 60:
            times = str(second) + "s"
        elif 3600 > second >= 60:
            m = int(second / 60)
            s = second % 60
            times = str(m) + "m" + str(int(s)) + "s"
        else:
            m, s = divmod(second, 60)
            h, m = divmod(m, 60)
            times = str(h) + "h" + str(m) + "m" + str(int(s)) + "s"
        return times


