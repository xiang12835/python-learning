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

p = Point(10, 10)
print p  # 尝试打印 Point 实例

print repr(p)  # 在打印 p 时其实是调用了 repr(p)
