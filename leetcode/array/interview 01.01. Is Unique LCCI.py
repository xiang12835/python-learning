# coding=utf-8


"""

mplement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

Example 1:

Input: s = "leetcode"
Output: false
Example 2:

Input: s = "abc"
Output: true


"""


class Solution(object):
    def isUnique(self, astr):
        """
        :type astr: str
        :rtype: bool

        for c in astr:
            if astr.count(c) > 1:
                return False

        return True

        """
        return len(astr) == len(set(astr))
