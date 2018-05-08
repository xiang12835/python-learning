# coding=utf-8
import datetime


def gen_dates(b_date, days):
    day = datetime.timedelta(days=1)
    for i in range(days):
        yield b_date + day*i


def get_date_list(start=None, end=None):
    """
    获取日期列表
    :param start: 开始日期
    :param end: 结束日期
    :return:
    """
    if start is None:
        start = datetime.datetime.strptime("2018-01-01", "%Y-%m-%d")
    if end is None:
        end = datetime.datetime.now()

    l = []
    for d in gen_dates(start, (end-start).days):
        l.append(d)
    return l


if __name__ == "__main__":

    start_time = "2018-04-08"
    end_time = "2018-05-08"

    if type(start_time) == str or type(start_time) == unicode:
        start_time = datetime.datetime.strptime(start_time, '%Y-%m-%d')

    if type(end_time) == str or type(end_time) == unicode:
        end_time = datetime.datetime.strptime(end_time, '%Y-%m-%d')

    print get_date_list(start_time, end_time)

