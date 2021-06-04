# coding=utf-8

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """dp

        1. subproblem

        2. dp array

        dp[i][j] 表示 text1[0:i] 和 text2[0:j] 的最长公共子序列的长度。

        3. dp equation

        当 text1[i - 1] == text2[j - 1] 时，dp[i][j] = 1 + dp[i - 1][j - 1]

        当 text1[i - 1] != text2[j - 1] 时，dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        T: O(logmn)
        S: O(logmn)
        """
        if not text1 or not text2:
            return 0

        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
