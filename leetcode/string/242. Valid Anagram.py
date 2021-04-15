# coding=utf-8

class Solution(object):
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


class Solution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        哈希表

        互为异位词 等价于 每一个字符的频数相同
        """
        import collections
        return collections.Counter(s) == collections.Counter(t)


class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        字母个数数组：用字数统计，因为只可能是26个字母

        T：O(n)，其中 n 为 s 的长度。
        S：O(S)，其中 S 为字符集大小，此处 S=26。
        """
        if len(s) != len(t):
            return False

        charCount = [0] * 26
        for i in s:
            charCount[ord(i) - ord('a')] += 1

        for j in t:
            charCount[ord(j) - ord('a')] -= 1
            if charCount[ord(j) - ord('a')] < 0:
                return False

        return True
