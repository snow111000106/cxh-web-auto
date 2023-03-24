# -*- coding: utf-8 -*-
# @Time    : 2022/10/08
# @Author  : chenxuehong
# @File    : redis_xhs.py

import redis


class CmmRedis:

    @staticmethod
    def redis_xiaohongshu():

        pool = redis.ConnectionPool(host='10.64.108.171', port=6379, db=1, password='CDStest.2018', decode_responses=True)
        con = redis.Redis(connection_pool=pool)
        return con

    @staticmethod
    def get_redis_value(key):
        """
        获取缓存中某个key的值
        """
        try:
            value = CmmRedis.redis_xiaohongshu().get(key)

        except Exception as e:
            print("Error!:{0}".format(e))

        return value

    @staticmethod
    def set_redis_value(key, value):
        """
        设置缓存中单个key的值为value
        """
        try:
            CmmRedis.redis_xiaohongshu().set(key, value=value)

        except Exception as e:
            print("Error!:{0}".format(e))


if __name__ == "__main__":
    pass
