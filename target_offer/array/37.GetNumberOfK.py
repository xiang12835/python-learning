# coding=utf-8

"""问题描述

统计一个数字在排序数组中出现的次数。

"""


class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        if k not in data:
            return 0

        count = 0
        for n in data:
            if n == k:
                count += 1
        return count
