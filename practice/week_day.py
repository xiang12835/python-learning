# coding=utf-8

import datetime


def get_week_day(date):
    week_day_dict = {
        0: '周一',
        1: '周二',
        2: '周三',
        3: '周四',
        4: '周五',
        5: '周六',
        6: '周日',
    }
    day = date.weekday()
    return week_day_dict[day]


what_day = get_week_day(datetime.datetime.now())
print what_day
