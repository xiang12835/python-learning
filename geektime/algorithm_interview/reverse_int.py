# coding=utf-8

"""

2、给定一个 32 位有符号整数，将整数中的数字进行反转。
Given a 32-bit signed integer, reverse digits of an integer.

"""

class Solution(object):
    def reverse_int(self, n):
        MAX_INT = pow(2, 31) - 1
        MIN_INT = -pow(2, 32)

        r = str(n)[::-1]

        if r[-1] == '-':
            r = r[-1] + r[:-1]

        r = int(r)

        if r > MAX_INT or r < MIN_INT:
            return 0

        return r
