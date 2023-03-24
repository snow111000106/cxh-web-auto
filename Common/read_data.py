# -*- coding: utf-8 -*-
# @Time    : 2022/11/15
# @Author  : chenxuehong
# @File    : read_data.py

import yaml


class ReadYaml:

    @staticmethod
    def read_yaml_data(file_path):
        # 解析yml文件数据
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)