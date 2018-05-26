# coding=utf-8

import datetime
import time
import re

DATE_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def string_to_datetime(datetime_str, _format=DATE_TIME_FORMAT):
    return datetime.datetime.strptime(datetime_str, _format)


def datetime_to_string(dt=datetime.datetime.now(), _format=DATE_TIME_FORMAT):
    return dt.strftime(_format)


def timestamp_to_datetime(response):
    """Converts a unix timestamp to a Python datetime object"""
    if not response:
        return None
    try:
        response = int(response)
    except ValueError:
        return None
    return datetime.datetime.fromtimestamp(response)


def datetime_to_timestamp(d):
    return int(time.mktime(d.timetuple()))


def human_readable_mseconds(mseconds):
    seconds = int(mseconds) / 1000
    s = seconds % 60
    h = seconds / 60 / 60

    if h:
        m = seconds / 60 % 60
        ret = u"%02d:%02d:%02d" % (h, m, s)

    else:
        m = seconds / 60
        ret = u"%02d:%02d" % (m, s)

    return ret


def zero_date():
    d = datetime.datetime.today()
    return datetime.datetime(d.year, d.month, d.day)


def days_ago(day=30):
    return datetime.datetime.now() - datetime.timedelta(day)


def nature_days_ago(day=30):
    return zero_date() - datetime.timedelta(day)


def after_days(day=30):
    return datetime.datetime.now() + datetime.timedelta(day)


def nature_after_days(day=30):
    return zero_date() + datetime.timedelta(day)


def seconds_to_zero():
    d = nature_after_days(1)
    return int(datetime_to_timestamp(d) - int(time.time()))


def is_weekend(d=datetime.datetime.today()):
    return d.weekday() in (0, 6)


def minutes_ago(seconds=300):
    return datetime.datetime.now() - datetime.timedelta(seconds=seconds)


def after_minutes(seconds=300):
    return datetime.datetime.now() + datetime.timedelta(seconds=seconds)


def int_day(d=None):
    if d is None:
        d = datetime.datetime.today()
    return int("%s%d%d" % (d.year, d.month, d.day))


def int_days(d=None):
    if d is None:
        d = datetime.datetime.today()
    return int("%s%02d%02d" % (d.year, d.month, d.day))


def int_month(d=None):
    if d is None:
        d = datetime.datetime.today()
    return int("%s%d" % (d.year, d.month))


def int_week(d=None):
    if d is None:
        d = datetime.datetime.today()

    monday = d.weekday()
    d = d - datetime.timedelta(monday)

    return int("%s%d%d" % (d.year, d.month, d.day))


def int_weeks(d=None):
    if d is None:
        d = datetime.datetime.today()

    monday = d.weekday()
    d = d - datetime.timedelta(monday)

    return int("%s%02d%02d" % (d.year, d.month, d.day))


def int_last_weeks(d=None):
    if d is None:
        d = datetime.datetime.today() - datetime.timedelta(7)

    monday = d.weekday()
    d = d - datetime.timedelta(monday)

    return int("%s%02d%02d" % (d.year, d.month, d.day))


def is_legal_date(d):
    time_re = "^(\d{2}|\d{4})-((0([1-9]{1}))|(1[0|1|2]))-(([0-2]([0-9]{1}))|(3[0|1]))$"
    return re.match(time_re, d) != None


""" 参考文档
http://python.usyiyi.cn/documents/python_352/library/time.html#module-time
http://python.usyiyi.cn/documents/python_352/library/datetime.html#module-datetime
"""



''' timedalte

timedalte 是datetime中的一个对象，该对象表示两个时间的差值

构造函数：datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
其中参数都是可选，默认值为0

下面应该是常识，几乎每个人都知道：



1 millisecond = 1000 microseconds
1 minute = 60 seconds
1 hour = 3600 seconds
1 week = 7 days



在构造函数中，参数值的范围如下：



0 <= microseconds < 1000000
0 <= seconds < 3600*24 (the number of seconds in one day)
-999999999 <= days <= 999999999


timedalte 有三个只读属性：



timedelta.min：负数最大时间差，相当于  timedelta(-999999999)。
timedelta.max：正数最大时间差，相当于  timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)。
timedelta.resolution：两个时间的最小差值 相当于   timedelta(microseconds=1)。


'''