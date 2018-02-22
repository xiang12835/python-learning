# coding=utf-8


"""题目描述

数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

"""


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        d = {}
        for n in numbers:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        for k, v in d.items():
            if v > len(numbers)/2:
                return k
        return 0
