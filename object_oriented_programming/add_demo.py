# coding=utf-8


class Point:
    def __init__(self, x=0, y=0):
        self.__x, self.__y = x, y

    def set(self, x, y):
        self.__x, self.__y = x, y

    def __f(self):
        pass

    def __repr__(self):
        return 'Point({}, {})'.format(self.__x, self.__y)

    def __add__(self, other):
        return Point(self.__x + other.__x, self.__y + other.__y)


# 两个坐标点相加是个很合理的需求。
p1 = Point(10, 10)
p2 = Point(10, 10)

p3 = p1 + p2

print p3
