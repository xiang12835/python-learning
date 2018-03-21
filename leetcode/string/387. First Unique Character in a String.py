"""
 Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in xrange(len(s)):
            if not s[i:i+1] in s[:i]+s[i+1:]:
                return i
        return -1


class Solution1(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for c in s:
            if s.count(c) == 1:
                return s.index(c)
        return -1


class Solution2(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        index_list = [s.index(c) for c in set(s) if s.count(c) == 1]
        return min(index_list) if index_list else -1

