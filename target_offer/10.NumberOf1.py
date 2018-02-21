# coding=utf-8

"""问题描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""

"""思路解析
考虑二进制1100，减1之后变为1011 1100&1011 为 1000，也就是说n和n-1的与运算，结果是将n的最后一位变成了0
"""

""" 补码

1. 正整数的补码是其二进制表示，与原码相同
2. -5对应正数5（00000101）→ 所有位取反（11111010）→ 加1(11111011)
所以-5的补码是11111011。
3. 数0的补码表示是唯一的
[+0]补=[+0]反=[+0]原=00000000
[ -0]补=11111111+1=00000000
"""


"""模
表示n位的计算机计量范围是0～2^(n)-1
所以32位计算机的模是2^(32)-1
"""


class Solution:
    def NumberOf1(self, n):
        # write code here
        if n < 0:  # 如果是负数求原码
            n = n & 0xffffffff
        count = 0
        while n:
            count += 1
            n = n & (n-1)
        return count


class Solution1:
    def NumberOf1(self, n):
        # write code here
        if n < 0:
            n = n + pow(2, 32)

        return bin(n).count("1")
