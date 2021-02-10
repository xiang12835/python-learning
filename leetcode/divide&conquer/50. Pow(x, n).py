# coding=utf-8

"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n

        r = 1
        while n:
            if n & 1:
                r *= x
            x *= x
            n >>= 1

        return r


class Solution1:
    def myPow(self, x: float, n: int) -> float:

        """
        暴力法

        T：O(n)
        S：O(1)

        """
        if n < 0:
            n = -n
            x = 1 / x

        r = 1
        for _ in range(n):
            r *= x

        return r


class Solution2:
    def myPow(self, x: float, n: int) -> float:
        """
        分治法

        T：O(logn)，即为递归的层数。
        S：O(logn)，即为递归的层数。这是由于递归的函数调用会使用栈空间。

        """
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


class Solution3:
    def myPow(self, x: float, n: int) -> float:
        """
        分治法

        T：O(logn)，即为递归的层数。
        S：O(logn)，即为递归的层数。这是由于递归的函数调用会使用栈空间。

        """

        if n < 0:
            n = -n
            x = 1 / x

        return self._dc(x, n)

    def _dc(self, x, n):
        # terminator
        if n == 0:
            return 1.0

        # process (split your big problems)
        half = self._dc(x, n // 2)

        # drill down (subproblems), merge (subresult)
        if n % 2 == 0:
            # even
            return half * half
        else:
            # odd
            return half * half * x

        # reverse states


