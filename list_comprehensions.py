# coding=utf-8


'''生成 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''
print list(range(1,11))


'''生成[1x1, 2x2, 3x3, ..., 10x10]'''
print [x*x for x in range(1, 11)]


'''筛选出仅偶数的平方'''
print [x*x for x in range(1, 11) if x%2 == 0]


'''使用两层循环，可以生成全排列'''
print [m + n for m in 'ABC' for n in '123']


'''列出当前目录下的所有文件和目录名'''
import os
print [d for d in os.listdir('.')]


'''for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value'''
d = {'x':'a', 'y':'b', 'z':'c'}
print [k + '=' + v for k, v in d. items()]


'''把一个list中所有的字符串变成小写'''
l = ['Hello', 'World']
print [s.lower() for s in l]


'''练习: 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错，请解决'''
l = ['Hello', 'World', 1, 'abc', None]
print [s.lower() for s in l if isinstance(s, str) ]
