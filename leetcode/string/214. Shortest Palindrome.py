# coding=utf-8

"""
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
"""

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        时间复杂度: O(N^2)
        空间复杂度: O(N)
        """
        for i in xrange(len(s), -1, -1):
            pref = s[:i]
            suff = s[i:]
            if pref == pref[::-1]:
                return suff[::-1] + s


class Solution1(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        for j in range(len(s)-1, -1, -1):
            if s[i] == s[j]:
                i += 1
        if i == len(s):
            return s
        tmp = s[i:][::-1]
        return tmp + self.shortestPalindrome(s[:i]) + s[i:]

