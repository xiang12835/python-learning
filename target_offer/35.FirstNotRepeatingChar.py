# coding=utf-8

"""题目描述

在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置

"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        l = list(s)
        for c in l:
            if s.count(c) == 1:
                return s.index(c)
        return -1


if __name__ == "__main__":
    s = Solution()
    print s.FirstNotRepeatingChar("google")
