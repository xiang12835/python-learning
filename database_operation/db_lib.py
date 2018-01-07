# coding=utf-8

from django.db import connections


def my_custom_stat_sql(sql):
    cursor = connections["statstic"].cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    return rows


def my_custom_sql(sql, db="bskgk_slave"):
    cursor = connections[db].cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    cursor.close()
    return rows


def my_custom_one_sql(sql, db="bskgk_slave"):
    cursor = connections[db].cursor()
    cursor.execute(sql)
    rows = cursor.fetchone()
    cursor.close()
    return rows


class SqlExecute(object):

    @classmethod
    def fetch_all(cls, sql, db="bskgk"):
        cursor = connections[db].cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        return rows

    @classmethod
    def fetch_one(cls, sql, db="bskgk"):
        cursor = connections[db].cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        cursor.close()
        return row

    @classmethod
    def execute_many(cls, sql, params, db="bskgk"):
        cursor = connections[db].cursor()
        cursor.executemany(sql, params)
        cursor.close()
