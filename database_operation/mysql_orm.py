# coding=utf-8

# pip install peewee

import peewee
from peewee import *

db = MySQLDatabase('mysql', user='your_username', passwd='your_password')


class Price(peewee.Model):
    timestamp = peewee.DateTimeField(primary_key=True)
    BTCUSD = peewee.FloatField()

    class Meta:
        database = db


def test_peewee():
    Price.create_table()
    price = Price(timestamp='2019-06-07 13:17:18', BTCUSD='12345.67')
    price.save()


