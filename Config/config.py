# -*- coding: utf-8 -*-
# @Time    : 2022/11/15
# @Author  : chenxuehong
# @File    : config.py


from Config.consts import environment
from Common.mylog import Mylog
from Common.read_data import ReadYaml


class Config:

    @staticmethod
    def get_url(path=''):
        web = ReadYaml.read_yaml_data(file_path='./Config/web.yaml')
        if environment == 'test':
            whole_url = web['home']['test']+path
        elif environment == 'stage':
            whole_url = web['home']['stage']+path
        elif environment == 'release':
            whole_url = web['home']['release']+path
        else:
            print('环境配置错误')
            Mylog.error("环境配置错误")
            raise
        return whole_url