# coding=utf-8

"""

Implement int sqrt(int x).

Compute and return the square root of x.

x is guaranteed to be a non-negative integer.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.


"""


"""思路解析

一个数 x 的开方 sqrt 一定在 0 ~ x 之间，并且满足 sqrt == x / sqrt 。可以利用二分查找在 0 ~ x 之间查找 sqrt。

"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int

        牛顿迭代法
        时间复杂度: O(logN) | 空间复杂度: O(1)
        """
        r = x
        while r * r > x:
            r = (r + x / r) / 2
        return r


class Solution1(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int

        迭代中的二分法
        时间复杂度: O(logN) | 空间复杂度: O(1)
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


if __name__ == "__main__":
    s = Solution()
    print s.mySqrt(100)

    s1 = Solution1()
    print s1.mySqrt(102)

