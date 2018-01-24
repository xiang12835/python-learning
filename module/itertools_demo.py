# coding=utf-8

import itertools


"""
groupby()把迭代器中相邻的重复元素挑出来放在一起
"""

for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group)

"""
实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
"""

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print key, list(group)
