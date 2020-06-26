# coding=utf-8

"""
将抛出异常和类做一个结合，通过 with 语句简化异常编写，可以让代码看起来更加简介
"""

class TestWith():
    def __enter__(self):
        print 'run'
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print '正常结束'
        else:
            print 'has error %s' % exc_tb

with TestWith():
    print 'Test is running'
    raise NameError('testNameError')
