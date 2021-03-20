# coding=utf-8

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int

        DP

        T: O(n)
        S: O(1)
        """
        if n < 2:
            return n

        a = 0
        b = 1
        r = 0
        for _ in range(2, n + 1):
            r = b + a
            a = b
            b = r

        return r