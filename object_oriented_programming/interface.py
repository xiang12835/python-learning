# coding=utf-8


# 用 python 实现一个接口

class AbstractShape:
    def area(self):
        raise NotImplementedError


a = AbstractShape()
try:
    a.area()
except NotImplementedError:
    pass
