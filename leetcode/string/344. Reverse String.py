# coding=utf-8
"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


class Solution1(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        左右对撞
        """

        ss = list(s)
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            ss[l], ss[r] = ss[r], ss[l]
            l += 1
            r -= 1

        return ''.join(ss)
