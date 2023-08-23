# -*- coding: utf-8 -*-
# @Time    : 2022/11/15
# @Author  : chenxuehong
# @File    : config.py


from Config.consts import environment
from Common.mylog import Mylog
from Common.read_data import ReadYaml


class Config:

    @staticmethod
    def get_url(path='', types='cxh'):
        web = ReadYaml.read_yaml_data(file_path='./Config/web_host.yaml')

        host_mapping = {
            'cxh': web['host'],
            'cmm': web['cmm_host'],
            'cgj': web['cgj_host']
        }
        if types not in host_mapping:
            print('host类型输入错误，请输入cxh/cmm/cgj')
            Mylog.error('host类型输入错误，请输入cxh/cmm/cgj')
            raise ValueError('host类型输入错误，请输入cxh/cmm/cgj')

        host = host_mapping[types][environment]
        whole_url = host + path

        return whole_url