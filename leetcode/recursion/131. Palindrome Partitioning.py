# coding=utf-8

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        - 时间复杂度: O(2^N)
        - 空间复杂度: O(2^N)
        """
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        if not s:
            res.append(path)
            return
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                print 's-->',s[i:]
                print 'path-->',path + [s[:i]]
                self.dfs(s[i:], path + [s[:i]], res)

    def isPalindrome(self, s):
        return s == s[::-1]


if __name__ == "__main__":
    s = "aab"
    r = Solution().partition(s)
    print r
