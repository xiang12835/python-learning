# coding=utf-8

import copy


a = [[1], ['a'], ['A']]

b = copy.copy(a)  # 创建新的复合对象并通过引用复制x的成员来创建x的浅复制。更加深层次说，它复制了对象,但对于对象中的元素,依然使用引用。
print "copy.copy() --> ", b
print "b is a", b is a
print "b == a", b == a
# [[1], ['a'], ['A']]

c = copy.deepcopy(a)  # 如果你想完全的拷贝一个对象和一个对象的所有元素的值，只有使用下面的deepcopy()函数。
print "copy.deepcopy() --> ", c
print "c is a", c is a
print "c == a", c == a
# [[1], ['a'], ['A']]

a[1].append('b')
print a
# [[1], ['a', 'b'], ['A']]
print b
# [[1], ['a', 'b'], ['A']]
print c
# [[1], ['a'], ['A']]

