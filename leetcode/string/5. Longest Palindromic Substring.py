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


class Solution1:
    def longestPalindrome(self, s: str) -> str:
        """
        DP

        T: O(n**2)
        S: O(n**2)
        """
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]


class Solution2(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str

        中心扩散法

        T: O(n**2)
        S: O(1)
        """
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)  # 奇数
            left2, right2 = self.expandAroundCenter(s, i, i + 1)  # 偶数
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1