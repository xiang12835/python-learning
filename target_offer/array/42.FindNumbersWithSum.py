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

        for i in range(len(array)-1):
            for j in range(i+1, len(array)):
                if sum([array[i], array[j]]) == tsum:
                    return [array[i], array[j]]
        return []


class Solution1:
    # Time: O(n*n)
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []

        left = 0
        right = len(array) - 1

        while left < right:
            if sum([array[left], array[right]]) < tsum:
                left += 1
            elif sum([array[left], array[right]]) > tsum:
                right -= 1
            else:
                return [array[left], array[right]]
        return []


if __name__ == "__main__":
    s = Solution1()
    print s.FindNumbersWithSum([1,2,4,7,11,15],15)
