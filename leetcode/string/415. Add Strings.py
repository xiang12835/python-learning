# coding=utf-8

"""

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str

        时间复杂度 O(max(M,N))：其中 M，N 为 2 数字长度，按位遍历一遍数字（以较长的数字为准）；
        空间复杂度 O(1)：指针与变量使用常数大小空间。

        """
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0

        res = ''
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            tmp = n1 + n2 + carry
            carry = tmp / 10
            res = str(tmp % 10) + res
            i -= 1
            j -= 1

        return '1' + res if carry else res


