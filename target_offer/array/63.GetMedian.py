# -*- coding:utf-8 -*-


"""题目描述

如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

"""


class Solution:
    def __init__(self):
        self.l = []
    def Insert(self, num):
        # write code here
        self.l.append(num)
        self.l.sort()
    def GetMedian(self, item):
        # write code here
        length = len(self.l)
        if length%2 == 1:
            return self.l[length/2]
        else:
            return (self.l[length/2 - 1] + self.l[length/2])/2.0
