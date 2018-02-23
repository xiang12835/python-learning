#!/usr/bin/python
# coding=utf-8

"""描述

cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。


"""


"""语法


以下是 cmp() 方法的语法:

cmp( x, y )

"""

"""返回值

如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 

"""


print "cmp(80, 100) : ", cmp(80, 100)
print "cmp(100, 100) : ", cmp(100, 100)
print "cmp(180, 100) : ", cmp(180, 100)
print "cmp(-80, 100) : ", cmp(-80, 100)
print "cmp(80, -100) : ", cmp(80, -100)
