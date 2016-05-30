# coding=utf-8

# 异常的引发
# 1/用raise引发一个系统的错误类
i=8
print i
if i>7:
    print 9
    raise NameError
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
