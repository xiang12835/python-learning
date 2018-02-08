# coding=utf-8


"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0

        stack = []
        l = []
        for i in str(x):
            if i == "-":
                l.append("-")
                continue
            stack.append(i)

        while stack:
            l.append(stack.pop())

        r = ("").join(l)

        r = int(r)

        if abs(r) > 0x7FFFFFFF:
            return 0

        return r


if __name__ == '__main__':
    s = Solution()
    print s.reverse(123)
    print s.reverse(-123)
    print s.reverse(120)


"""
在C语言里，整数有三种表示形式：十进制，八进制，十六进制。
其中以数字0开头，由0~7组成的数是八进制。以0X或0x开头，由0~9，A~F或a~f 组成是十六进制。除表示正负的符号外，以1~9开头，由0~9组成是十进制。
1.十进制：除表示正负的符号外，以1~9开头，由0~9组成。如，128，+234，-278。
2,八进制：以0开头，由0~7组成的数。如，0126,050000.
3,十六进制：以0X或0x开头，由0~9，A~F或a~f 组成。如，0x12A,0x5a000.


可以算一下 0x7FFFFFFF 是多少
每个十六进制数4bit，因此8位16进制是4个字节，刚好是一个int整型
F的二进制码为 1111
7的二进制码为 0111
这样一来，整个整数 0x7FFFFFFF 的二进制表示就是除了首位是 0，其余都是1
就是说，这是最大的整型数 int（因为第一位是符号位，0 表示他是正数）
用 INT_MAX 常量可以替代这个值。
~0取反：表示最小值。
～0u表示无符号整形0
~0 >> 1 ：表示最大值

"""
