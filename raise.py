# coding=utf-8

# 异常的引发
# 1/用raise引发一个系统的错误类
i=8
print i
if i>7:
    print 9
    # raise NameError
    print 10

# 2/自定义一个异常并用raise引发
class RhhError(Exception):                 #按照命名规范，以Error结尾，并且自定义异常需要继承Exception类
    def __init__(self):
        Exception.__init__(self)
try:
    i=8
    if i>7:
        raise RhhError()
except RhhError,a:
    print "RhhError:错了就是错了"


# 3/自定义一个多参数的异常并用raise引发，比如我们可以定义一个异常，当x>2或者x+y>7的时候都会引发该异常


# 如果要抛出错误，
# 1) 首先根据需要，可以定义一个错误的class，选择好继承关系，
# 2) 然后，用raise语句抛出一个错误的实例
# class FooError(ValueError):
#     pass
#
# def foo(s):
#     n = int(s)
#     if n==0:
#         raise FooError('invalid value: %s' % s)
#     return 10 / n
#
# foo('0')


# 捕获错误目的只是记录一下，便于后续追踪。
# 但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()

