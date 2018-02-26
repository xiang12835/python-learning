# coding=utf-8

"""题目描述

输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

输出描述:

对应每个测试案例，输出两个数，小的先输出。

"""


class Solution:
    # Time: O(n*n)
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        index = 0
        r = []
        while index < len(array):
            for i in range(index+1, len(array)):
                if sum([array[index], array[i]]) == tsum:
                    r.append(array[index])
                    r.append(array[i])
                    return r
            index += 1
        return []


if __name__ == "__main__":
    s = Solution()
    print s.FindNumbersWithSum([1,2,4,7,11,15],15)
