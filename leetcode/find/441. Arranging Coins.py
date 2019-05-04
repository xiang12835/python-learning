#coding=utf-8

"""

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
"""


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        二分查找法，因为数列是等差数列，看成排序数组，找到前n项和等于n
        """
        l, r = 0, n
        while l <= r:
            mid = (l + r) / 2
            s = mid * (mid + 1) / 2
            if n == s:
                return mid
            elif n > s:
                l = mid + 1
            else:
                r = mid - 1

        return r
