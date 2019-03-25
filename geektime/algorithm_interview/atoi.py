# coding=utf-8

"""

3、实现 atoi，将字符串转为整数。
Implement atoi which converts a string to an integer.

"""

class Solution(object):
    def myAtoi(self, s):
        MIN_MAX = -pow(2, 31)
        MAX_INT = pow(2, 31) - 1

        s = s.strip()
        if not s:
            return 0

        # 判断符号
        sign = 1
        if s[0] in ['+', '-']:

            if s[0] == '-':
                sign = -1

            s = s[1:]

        r = 0
        for c in s:
            if c.isdigit():
                r = r * 10 + int(c)
            else:  # 连续
                break

        r *= sign

        if r < MIN_MAX:
            r = MIN_MAX

        if r > MAX_INT:
            r = MAX_INT

        return r
