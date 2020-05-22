# coding=utf-8

"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        T: O(n^2)
        S: O(1)
        """
        if s == s[::-1]:
            return s

        n = len(s)
        max_len = 1
        r = s[0]
        for i in range(n - 1):
            for j in range(i + 1, n):
                if j - i + 1 > max_len and s[i:j + 1] == s[i:j + 1][::-1]:
                    max_len = j - i + 1
                    r = s[i:j + 1]
        return r
