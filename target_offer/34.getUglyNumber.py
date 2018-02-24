# coding=utf-8

"""题目描述

把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

"""


class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        found = 0
        num = 0
        while found < index:
            if self.isUgly(num):
                found += 1
            num += 1

    def isUgly(self, num):
        while num % 2 == 0:
            num /= 2
        while num % 3 == 0:
            num /= 3
        while num % 5 == 0:
            num /=5
        return True if num == 1 else False

