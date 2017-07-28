# coding=utf-8


class Point:
    def __init__(self, x=0, y=0):
        self.__x, self.__y = x, y

    def set(self, x, y):
        self.__x, self.__y = x, y

    def __f(self):
        pass

p = Point(10, 10)
try:
    p.__x   # __x、__y 和 __f 就相当于私有了
except Exception as e:
    print e

print p._Point__x
