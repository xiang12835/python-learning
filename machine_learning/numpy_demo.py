# coding=utf-8

"""
用于高性能科学计算和数据分析， 是常用的高级数据分析库的基础包
"""

import numpy as np

arr1 = np.array([2,3,4])
print arr1
print arr1.dtype

arr2 = np.array([2.1,3.1,4.1])
print arr2
print arr2.dtype

print arr1 + arr2
print arr1 * 10

# 二维矩阵
arr3 = np.array([[1,2,3],[2,3,4]])
print arr3
print arr3.dtype
