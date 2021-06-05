# coding=utf-8

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        https://leetcode-cn.com/problems/distinct-subsequences/solution/dong-tai-gui-hua-yi-ci-ti-wei-li-jiang-j-enq0/

        1. subproblem

        2. dp array

        dp元素的含义是t的前i个字符与s的前j个字符成功匹配的个数

        3. dp equation

        如果t[i-1] == s[j-1]，dp[i][j] = dp[i][j-1] + dp[i-1][j-1];
        如果t[i-1] != s[j-1]，dp[i][j] = dp[i][j-1]

        T: O(mn)
        S: O(mn)
        """

        m = len(t)
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(n + 1):
            dp[0][i] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t[i - 1] == s[j - 1]:  # 易错，下标
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[-1][-1]
