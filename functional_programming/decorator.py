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



# 例子：输出函数执行时间的装饰器。
import time
def timeit(func):
  def wrapper():
    start = time.clock()
    func()
    end =time.clock()
    print 'used:', end - start
    return wrapper

@timeit
def foo():
  print 'in foo()'


########## 装饰器的嵌套 ##########
print '=' * 20

import functools

def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator1')
        # print "run_func", func.__name__
        func(*args, **kwargs)
    return wrapper


def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator2')
        # print "run_func", func.__name__
        func(*args, **kwargs)
    return wrapper


@my_decorator1
@my_decorator2
def greet(message):
    print(message)


# 等效于 decorator1(decorator2(func))


greet('hello world')



"""身份认证

首先是最常见的身份认证的应用。这个很容易理解，举个最常见的例子，你登录微信，需要输入用户名密码，然后点击确认，这样，服务器端便会查询你的用户名是否存在、是否和密码匹配等等。如果认证通过，你就可以顺利登录；如果不通过，就抛出异常并提示你登录失败。

再比如一些网站，你不登录也可以浏览内容，但如果你想要发布文章或留言，在点击发布时，服务器端便会查询你是否登录。如果没有登录，就不允许这项操作等等。

import functools

def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        if check_user_logged_in(request): # 如果用户处于登录状态
            return func(*args, **kwargs) # 执行函数 post_comment() 
        else:
            raise Exception('Authentication failed')
    return wrapper
    
@authenticate
def post_comment(request, ...)
    ...

这段代码中，我们定义了装饰器 authenticate；而函数 post_comment()，则表示发表用户对某篇文章的评论。每次调用这个函数前，都会先检查用户是否处于登录状态，如果是登录状态，则允许这项操作；如果没有登录，则不允许。

"""


"""日志记录

日志记录同样是很常见的一个案例。在实际工作中，如果你怀疑某些函数的耗时过长，导致整个系统的 latency（延迟）增加，所以想在线上测试某些函数的执行时间，那么，装饰器就是一种很常用的手段。

import time
import functools

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 1000))
        return res
    return wrapper
    
@log_execution_time
def calculate_similarity(items):
    ...
    
这里，装饰器 log_execution_time 记录某个函数的运行时间，并返回其执行结果。如果你想计算任何函数的执行时间，在这个函数上方加上

"""


"""输入合理性检查

在大型公司的机器学习框架中，我们调用机器集群进行模型训练前，往往会用装饰器对其输入（往往是很长的 json 文件）进行合理性检查。这样就可以大大避免，输入不正确对机器造成的巨大开销。

import functools

def validation_check(input):
    @functools.wraps(func)
    def wrapper(*args, **kwargs): 
        ... # 检查输入是否合法
    
@validation_check
def neural_network_training(param1, param2, ...):
    ...

其实在工作中，很多情况下都会出现输入不合理的现象。因为我们调用的训练模型往往很复杂，输入的文件有成千上万行，很多时候确实也很难发现。

试想一下，如果没有输入的合理性检查，很容易出现“模型训练了好几个小时后，系统却报错说输入的一个参数不对，成果付之一炬”的现象。这样的“惨案”，大大减缓了开发效率，也对机器资源造成了巨大浪费。

"""


"""缓存

正确使用缓存装饰器，往往能极大地提高程序运行效率。为什么呢？我举一个常见的例子来说明。

大型公司服务器端的代码中往往存在很多关于设备的检查，比如你使用的设备是安卓还是 iPhone，版本号是多少。这其中的一个原因，就是一些新的 feature，往往只在某些特定的手机系统或版本上才有（比如 Android v200+）。

这样一来，我们通常使用缓存装饰器，来包裹这些检查函数，避免其被反复调用，进而提高程序运行效率，比如写成下面这样：

@lru_cache
def check(param1, param2, ...) # 检查用户设备类型，版本号等等
    ...

"""