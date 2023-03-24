# -*- coding: utf-8 -*-
# @Time    : 2021/12/01
# @Author  : chenxubin
# @File    : Base.py

"""
封装常用的方法
"""
import os
import hashlib
import time
import hmac
import base64
import urllib.parse
from dingtalkchatbot.chatbot import DingtalkChatbot
from Config.consts import webhook, secret, at_phone


class DingNotic:

    @staticmethod
    def dingding_notice():
        # 钉钉通知
        timestamp = str(round(time.time() * 1000))
        secret_enc = secret.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, secret)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        webhook_all = webhook + "&timestamp=" + timestamp + "&sign=" + sign
        xiaoding = DingtalkChatbot(webhook_all)
        xiaoding.send_text(msg=os.getenv("REPORT"), at_mobiles=at_phone)