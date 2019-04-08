# coding=utf-8

"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2

示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。
"""


class Solution1(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int

        # 二分查找
        # 时间复杂度: O(logN) | 空间复杂度: O(1)
        """
        if x == 0 or x == 1:
            return x

        l = 1
        r = x

        while l <= r:
            m = (l + r) / 2
            if m * m == x:
                return m
            elif m * m > x:
                r = m - 1
            else:
                l = m + 1
        return r  # 当无整数平方根时，取小值



class Solution2(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int

        # 牛顿迭代法
        # 时间复杂度: O(logN) | 空间复杂度: O(1)

        """
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r


