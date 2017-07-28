# coding=utf-8


class Point:
    def __init__(self, x=0, y=0):
        self.__x, self.__y = x, y

    def set(self, x, y):
        self.__x, self.__y = x, y

    def __f(self):
        pass

    def __str__(self):
        return '({}, {})'.format(self.__x, self.__y)

p = Point(10, 10)
print p  # 尝试打印 Point 实例

print str(p)  # 在打印 p 时其实是调用了 repr(p)


""" __repr__ 与 __str__ 的区别
repr() 的结果面向的是解释器，通常都是合法的 Python 代码，比如 Point(10, 10)；
而 str() 的结果面向用户，更简洁，比如 (10, 10)。
"""