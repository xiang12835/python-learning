# coding=utf-8

"""

pandas 用于数据的预处理和数据清洗

pandas库 数据分析库

使用 Series 操作一维数组，有点想字典

使用 DataFrame 操作操作二维或高维数组，有点像电子表格

"""

from pandas import Series, DataFrame
import pandas as pd

obj = Series([4,5,6,7.1])

print obj
print obj.index
print obj.values


obj1 = Series([4,5,6,7.1], index=['a', 'b', 'c', 'a'])  # 由索引和数值组成，索引不唯一，注意与字典的 key 区别
print obj1

obj2 = Series([4,5,6,7.1], index=['a', 'b', 'c', 'a'])
obj2['a'] = 9
print obj2
print 'f' in obj2


# 将字典转化为 Series
sdata = {
    'beijing': 35000,
    'shanghai': 71000,
    'guangzhou': 16000,
    'shenzhen': 5000
}
obj3 = Series(sdata)
print obj3

obj3.index = ['bj', 'gz', 'sh', 'sz']
print obj3

