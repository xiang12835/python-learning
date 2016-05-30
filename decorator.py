# -*- coding: utf-8 -*-

import functools

def log(func):
    @functools.wraps(func) # 相当于wrapper.__name__ = func.__name__，否则，有些依赖函数签名的代码执行就会出错
    def wrapper(*args, **kw):  # wrapper()函数可以接受任意参数的调用
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2016-5-28')

now() # now = log(now)

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@logger('DEBUG')
def today():
    print('2016-5-28')

today() # today = today('DEBUG')(today)
print(today.__name__)

'''练习: 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。'''
