# coding=utf-8


# 用字典推导式构建字典序列
l = [("a", 1), ["b", 2]]
d = {key: value for (key, value) in l}
print d
print dict(l)


# 用zip()构建字典序列
a = [1, 2, 3]
b = ['a', 'b', 'c']
lst = zip(a, b)
print lst

dic = dict(lst)
print dic
