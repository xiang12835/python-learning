# coding=utf-8


class Person:
    name = "aaa"

p1 = Person()
p2 = Person()
p1.name = "bbb"
print p1.name  # bbb
print p2.name  # aaa
print Person.name  # aaa


"""
类变量就是供类使用的变量,实例变量就是供实例使用的.

这里p1.name="bbb"是实例调用了类变量,这其实和上面第一个问题一样,就是函数传参的问题,
p1.name一开始是指向的类变量name="aaa",但是在实例的作用域里把类变量的引用改变了,就变成了一个实例变量,self.name不再引用Person的类变量name了.
"""


class Person_list:
    name = []

p3 = Person_list()
p4 = Person_list()
p3.name.append(1)
print p3.name  # [1]
print p4.name  # [1]
print Person_list.name  # [1]
