#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print('Point:', p.x, p.y)

'''
可以验证创建的Point对象是tuple的一种子类：

>>> isinstance(p, Point)
True
>>> isinstance(p, tuple)
True
'''

# 类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
# namedtuple('名称', [属性list]):
Circle = namedtuple('Circle', ['x', 'y', 'r'])




# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)


from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print('dd[\'key1\'] =', dd['key1'])
print('dd[\'key2\'] =', dd['key2'])



# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print d # dict的Key是无序的
# {'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od # OrderedDict的Key是有序的
# OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print list(od.keys()) # 按照插入的Key的顺序返回
# ['z', 'y', 'x']



# Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
# Counter({'g': 2, 'm': 2, 'r': 2, 'a': 1, 'i': 1, 'o': 1, 'n': 1, 'p': 1})

nums = [1, 2, 3, 4, 5]
print Counter(nums)
