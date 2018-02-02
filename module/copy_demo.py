# coding=utf-8

import copy


a = [[1], ['a'], ['A']]

b = copy.copy(a)  # copy对于一个复杂对象的子对象并不会完全复制。更加深层次说，它复制了对象,但对于对象中的元素,依然使用引用。
print "copy.copy() --> ", b
print "b is a", b is a
print "b == a", b == a
# [[1], ['a'], ['A']]

c = copy.deepcopy(a)  # deepcopy的时候会将复杂对象的每一层复制一个单独的个体出来。
print "copy.deepcopy() --> ", c
# [[1], ['a'], ['A']]

print "c is a", c is a
print "c == a", c == a

print "c is b", c is b
print "c == b", c == b

a[1].append('b')
print a
# [[1], ['a', 'b'], ['A']]
print b
# [[1], ['a', 'b'], ['A']]
print c
# [[1], ['a'], ['A']]

