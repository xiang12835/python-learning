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
print [k + '=' + v for k, v in d.items()]


'''把一个list中所有的字符串变成小写'''
l = ['Hello', 'World']
print [s.lower() for s in l]


'''练习: 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错，请解决'''
l = ['Hello', 'World', 1, 'abc', None]
print [s.lower() for s in l if isinstance(s, str)]


# 列表推导式
''' 1) 使用列表推导式来取代map和filter '''
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# use map
squares = map(lambda x: x ** 2, a)
# use list comprehension
squares = [x ** 2 for x in a]
# 一个很大的好处是，列表推导式可以对值进行判断，比如
squares = [x ** 2 for x in a if x % 2 == 0]
# 而如果这种情况要用 map 或者 filter 方法实现的话，则要多写一些函数

''' 2) 不要使用含有两个以上表达式的列表推导式 '''
# 有一个嵌套的列表，现在要把它里面的所有元素扁平化输出
list = [[
  [1, 2, 3],
  [4, 5, 6]
]]
# 使用列表推导式
flat_list = [x for list0 in list for list1 in list0 for x in list1]
# [1, 2, 3, 4, 5, 6]

# 可读性太差，易出错。这种时候更建议使用普通的循环
flat_list = []
for list0 in list:
    for list1 in list0:
        flat_list.extend(list1)

''' 3) 数据多时，列表推导式可能会消耗大量内存，此时建议使用生成器表达式 '''
# 在列表推导式的推导过程中，对于输入序列的每个值来说，都可能要创建仅含一项元素的全新列表。因此数据量大时很耗性能。
# 使用生成器表达式
list = (x ** 2 for x in range(0, 1000000000))
# 生成器表达式返回的迭代器，只有在每次调用时才生成值，从而避免了内存占用
