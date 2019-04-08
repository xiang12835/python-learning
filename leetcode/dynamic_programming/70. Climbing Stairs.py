# coding=utf-8


"""

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output:  2
Explanation:  There are two ways to climb to the top.

1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output:  3
Explanation:  There are three ways to climb to the top.

1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        if n == 2:
            return 2

        l = [1, 2]
        for _ in xrange(3, n + 1):
            l.append(l[-2] + l[-1])

        return l[-1]


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int

        dp[n] = dp[n-1] + dp[n+2]

        dp[0] = 1
        dp[1] = 1

        fibnacci数列

        """
        if n == 1:
            return 1

        x = 1
        y = 1

        r = 0

        for _ in xrange(2, n + 1):
            r = x + y

            x = y
            y = r
        return r
