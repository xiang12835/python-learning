# coding=utf-8

"""
all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否不为 0、''、False 或者 iterable 为空，如果是返回 True，否则返回 False。

如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；

注意：空元组、空列表返回值为True，这里要特别注意。
"""
print all(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0
print all(['a', 'b', '', 'd'])  # 列表list，存在一个为空的元素
print all([0, 1, 2, 3])  # 列表list，存在一个为0的元素
print all(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0
print all(('a', 'b', '', 'd'))  # 元组tuple，存在一个为空的元素
print all((0, 1, 2, 3))  # 元组tuple，存在一个为0的元素
print all([])  # 空列表
print all(())  # 空元组
