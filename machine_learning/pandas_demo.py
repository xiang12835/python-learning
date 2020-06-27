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


data = {'city': ['shanghai', 'shanghai', 'shanghai', 'beijing', 'beijing'],
        'year': [2016, 2017, 2018, 2017, 2018],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame = DataFrame(data)

# 排序
frame2 = DataFrame(data, columns=['year', 'city', 'pop'])


print frame
print frame2

# 将二维转一维
print frame2['city']
print frame2.year

# 增加新列
frame2['new'] = 100
print(frame2)


# 通过计算，生成新列
frame2['cap'] = frame2.city == 'beijing'
print(frame2)


pop = {'beijing': {2008: 1.5, 2009: 2.0},
       'shanghai': {2008: 2.0, 2009: 3.6}
       }

frame3 = DataFrame(pop)
print frame3

# 行列互换，转置
print frame3.T


obj4 = Series([4.5, 7.2, -5.3, 3.6], index=['b', 'd', 'c', 'a'])

obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'])
print obj5

# 对缺失的值进行填充
obj5 = obj4.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)
print obj5

obj6 = Series(['blue', 'purple', 'yellow'], index=[0, 2, 4])
print obj6

# 将前面的值进行填充
print obj6.reindex(range(6),method='ffill')

# 将后面的值进行填充
print obj6.reindex(range(6),method='bfill')


# 在 Series 中的删除缺失值
from numpy import nan as NA
data = Series([1, NA, 2])
print data
print data.dropna()


#  在 DataFrame 中的删除缺失值
data2 = DataFrame([[1., 6.5, 3], [1., NA, NA], [NA, NA, NA]])

print data2
print data2.dropna()  # 只要出现 NA，都会删掉

print data2.dropna(how='all')  # 删掉全是 NA 的行

data2[4] = NA
print data2
print data2.dropna(axis=1, how='all')  # 删掉全是 NA 的列

# 对缺失值进行填补
data3 = data2.fillna(0)  # 修改的副本
print data2
print data3

print data2.fillna(0, inplace=True)  # 对原有的数据进行修改
print data2

