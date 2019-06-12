# coding=utf-8


"""问题描述

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007

"""

"""思路解析

使用归并排序的思路进行求解

"""


# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return 0

        temp = [i for i in data]
        return self.mergeSort(temp, data, 0, len(data) - 1) % 1000000007

    def mergeSort(self, temp, data, low, high):
        if low >= high:
            temp[low] = data[low]
            return 0

        mid = (low + high) / 2
        left = self.mergeSort(data, temp, low, mid)
        right = self.mergeSort(data, temp, mid + 1, high)

        i = mid  # i初始化为前半段最后一个数字的下标
        j = high  # j初始化为后半段最后一个数字的下标
        index = high  # 辅助数组复制的数组的最后一个数字的下标

        count = 0  # 计数，逆序对的个数

        while i >= low and j >= mid + 1:
            if data[i] >= data[j]:
                temp[index] = data[i]
                count += j - mid  # 逆序对
                i -= 1
            else:
                temp[index] = data[j]
                j -= 1
            index -= 1

        while i >= low:
            temp[index] = data[i]
            i -= 1
            index -= 1

        while j >= mid + 1:
            temp[index] = data[j]
            j -= 1
            index -= 1
        return count + left + right
