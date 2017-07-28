# coding=utf-8


class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def set(self, x, y):  # self 并不是关键字，甚至可以用其它名字替代，比如 this
        self.x, self.y = x, y


p = Point(10, 10)  # __init__ 被调用

# Point 是 type 的一个实例，这和 p 是 Point 的一个实例是一回事Point 是 type 的一个实例，这和 p 是 Point 的一个实例是一回事
print type(p)
print type(Point)


print dir(Point)  # ['__doc__', '__init__', '__module__', 'set']
print Point.__module__


# p.set(...) 其实只是一个语法糖，你也可以写成 Point.set(p, ...)，这样就能明显看出 p 就是 self 参数了：
print p.x, p.y
p.set(0, 0)
print p.x, p.y
Point.set(p, 1, 1)
print p.x, p.y
