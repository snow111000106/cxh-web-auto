# -*- coding: utf-8 -*-
# @Time    : 2022/08/16
# @Author  : chenxuehong
# @File    : mysql_xhs.py

import pymysql


class CmmMysql:

    @staticmethod
    def db_xiaohongshu(sql):

        db = pymysql.connect(host='xxxxx',
                             port=xxxx,
                             user='xxx',
                             passwd='xxxx',
                             db='xxxx')
        cur = db.cursor()
        try:
            cur.execute(sql)
            re = cur.fetchall()
        except Exception as e:
            db.rollback()  # 如有异常回滚数据库并抛出异常
            print("Error!:{0}".format(e))
        finally:
            cur.close()
            db.close()
        return re

    @staticmethod
    def db_douyin(sql):

        db = pymysql.connect(host='xxxx',
                             port=xxx,
                             user='xxxx',
                             passwd='xxxx',
                             db='xxxx')
        cur = db.cursor()
        try:
            cur.execute(sql)
            re = cur.fetchall()
        except Exception as e:
            db.rollback()  # 如有异常回滚数据库并抛出异常
            print("Error!:{0}".format(e))
        finally:
            cur.close()
            db.close()
        return re


if __name__ == "__main__":
    pass
