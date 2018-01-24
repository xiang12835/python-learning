# coding=utf-8

import itertools


"""
groupby()把迭代器中相邻的重复元素挑出来放在一起
"""

for key, group in itertools.groupby('AAABBBCCAAA'):
    print key, list(group)
