# coding = utf-8


""" 题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
"""


"""

"""


class Solution:
    # 递归
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.Fibonacci(n-1) + self.Fibonacci(n-2)


class Solution1:
    # Time: O(n)
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0

        if n == 1:
            return 1

        first = 0
        second = 1
        r = 0
        for i in xrange(2, n+1):
            r = first + second

            first = second
            second = r

        return r
