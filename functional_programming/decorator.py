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




# 使用装饰器
''' 1
装饰器用于在不改变原函数代码的情况下修改已存在的函数。常见场景是增加一句调试，或者为已有的函数增加log监控
'''

def decorator_fun(fun):
    def new_fun(*args, **kwargs):
        print('current fun:', fun.__name__)
        print('position arguments:', args)
        print('key arguments:', kwargs)
        result = fun(*args, **kwargs)
        print(result)
        return result
    return new_fun


@decorator_fun
def add(a, b):
    return a + b


add(3, 2)
# current fun: add
# position arguments: (3, 2)
# key arguments: {}
# 5

''' 2
除此以外，还可以编写接收参数的装饰器，其实就是在原本的装饰器上的外层又嵌套了一个函数：
'''

def read_file(filename='results.txt'):
    def decorator_fun(fun):
        def new_fun(*args, **kwargs):
            result = fun(*args, **kwargs)
            with open(filename, 'a') as f:
                f.write(result + '\n')
            return result
        return new_fun
    return decorator_fun


# 使用装饰器时代入参数
@read_file(filename='log.txt')
def add(a, b):
    return a + b

''' 3
但是像上面那样使用装饰器的话有一个问题：
'''

@decorator_fun
def add(a, b):
    return a + b


print(add.__name__)
# new_fun

# 也就是说原函数已经被装饰器里的new_fun函数替代掉了。调用经过装饰的函数，相当于调用一个新函数。查看原函数的参数、注释、甚至函数名的时候，只能看到装饰器的相关信息。
# 为了解决这个问题，我们可以使用 Python 自带的functools.wraps方法。
# functools.wraps是个很 hack 的方法，它本事作为一个装饰器，做用在装饰器内部将要返回的函数上。
# 也就是说，它是装饰器的装饰器，并且以原函数为参数，作用是保留原函数的各种信息，使得我们之后查看被装饰了的原函数的信息时，可以保持跟原函数一模一样。


from functools import wraps

def decorator_fun(fun):
    @wraps(fun)
    def new_fun(*args, **kwargs):
        result = fun(*args, **kwargs)
        print(result)
        return result

    return new_fun


@decorator_fun
def add(a, b):
    return a + b


print(add.__name__)
# add

''' 4
此外，有时候我们的装饰器里可能会干不止一个事情，此时应该把事件作为额外的函数分离出去。但是又因为它可能仅仅和该装饰器有关，所以此时可以构造一个装饰器类。
原理很简单，主要就是编写类里的__call__方法，使类能够像函数一样的调用。
'''

from functools import wraps


class logResult(object):
    def __init__(self, filename='results.txt'):
        self.filename = filename

    def __call__(self, fun):
        @wraps(fun)
        def new_fun(*args, **kwargs):
            result = fun(*args, **kwargs)
            with open(self.filename, 'a') as f:
                f.write(result + '\n')
            return result

        self.send_notification()
        return new_fun

    def send_notification(self):
        pass


@logResult('log.txt')
def add(a, b):
    return a + b



def dec(f):
    n = 3
    def wrapper(*args,**kw):
        return f(*args,**kw) * n
    return wrapper

@dec
def foo(n):
    return n * 2

print foo(2)
print foo(3)

