# coding=utf-8

"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""


class Solution(object):
    def count_ch(self, s):
        d = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 0
        return d

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1 = self.count_ch(s)
        d2 = self.count_ch(t)
        return d1 == d2


class Solution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        import collections
        return collections.Counter(s) == collections.Counter(t)


class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        排序

        T: O(NlogN)
        S: O(logN)

        """
        return sorted(s) == sorted(t)


class Solution3(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        哈希表：用字数统计，因为只可能是26个字母

        T：O(n)，其中 n 为 s 的长度。
        S：O(S)，其中 S 为字符集大小，此处 S=26。

        """
        if len(s) != len(t):
            return False

        charCnt = [0] * 26

        for i in range(len(s)):
            charCnt[ord(s[i]) - 97] += 1
            charCnt[ord(t[i]) - 97] -= 1

        for cnt in charCnt:
            if cnt != 0:
                return False
        return True


class Solution4(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        哈希表：用字数统计，因为只可能是26个字母

        T：O(n)，其中 n 为 s 的长度。
        S：O(S)，其中 S 为字符集大小，此处 S=26。

        """
        if len(s) != len(t):
            return False

        charCnt = [0] * 26

        for i in range(len(s)):
            charCnt[ord(s[i]) - 97] += 1

        for i in range(len(t)):
            charCnt[ord(t[i]) - 97] -= 1
            if charCnt[ord(t[i]) - 97] < 0:
                return False

        return True

