# -*- coding: utf-8 -*-
# @Time    : 2022/11/15
# @Author  : chenxuehong
# @File    : config.py


from Config.consts import environment
from Common.mylog import Mylog
from Common.read_data import ReadYaml


class Config:

    @staticmethod
    def get_url(path='', types='蝉小红'):
        web = ReadYaml.read_yaml_data(file_path='./Config/path.yaml')

        host_mapping = {
            '蝉小红': web['host'],
            '蝉妈妈': web['cmm_host'],
            '蝉管家': web['cgj_host']
        }
        if types not in host_mapping:
            print('host类型输入错误，请输入cxh/cmm/cgj')
            Mylog.error('host类型输入错误，请输入cxh/cmm/cgj')
            raise ValueError('host类型输入错误，请输入cxh/cmm/cgj')

        host = host_mapping[types][environment]
        whole_url = host + path

        return whole_url

    @staticmethod
    def get_account_info(types='蝉小红', account_types='DEFAULT', account=0, pwd=0):
        accounts = ReadYaml.read_yaml_data(file_path='./Config/accounts.yaml')
        mapping = {
            '蝉小红': accounts['CXH'],
            '蝉妈妈': accounts['CMM'],
            '蝉管家': accounts['CGJ']
        }
        account_name = mapping[types][account_types][environment]
        account_pwd = mapping[types]['PASSWORD'][environment]
        if account == 1:
            return account_name
        if pwd == 1:
            return account_pwd
