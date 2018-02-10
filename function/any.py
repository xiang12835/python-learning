# coding=utf-8


"""
any() 函数用于判断给定的可迭代参数 iterable 是否全部为空对象，如果都为空、0、false，则返回 False，如果不都为空、0、false，则返回 True。


函数等价于：

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
"""

print any(['a', 'b', 'c', 'd'])  # 列表list，元素都不为空或0

print any(['a', 'b', '', 'd'])  # 列表list，存在一个为空的元素

print any([0, '', False])  # 列表list,元素全为0,'',false

print any([1, '', False])  # 列表list,元素全为0,'',false

print any([0, '1', False])  # 列表list,元素全为0,'',false

print any(('a', 'b', 'c', 'd'))  # 元组tuple，元素都不为空或0

print any(('a', 'b', '', 'd'))  # 元组tuple，存在一个为空的元素

print any((0, '', False))  # 元组tuple，元素全为0,'',false

print any([])  # 空列表

print any(())  # 空元组

