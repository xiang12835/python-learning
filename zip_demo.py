# coding=utf-8


x = [1,2,3]
y = [4,5,6]
z = [7,8,9]

xyz = zip(x,y,z)

print xyz


# 实例：构建字典序列
a = [1,2,3]
b = ['a','b','c']
lst = zip(a,b)
print lst

dic = dict(lst)
print dic
