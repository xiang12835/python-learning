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
        """
        if x < 1:
            return x

        l, r = 1, x
        while l <= r:
            mid = (l + r) / 2
            sqrt = x / mid
            if sqrt == mid:
                return mid
            elif sqrt < mid:
                r = mid - 1
            else:
                l = mid + 1


if __name__ == "__main__":
    s = Solution()
    print s.mySqrt(100)

    s1 = Solution1()
    print s1.mySqrt(100)
