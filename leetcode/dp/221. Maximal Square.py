# coding=utf-8

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """
        1. subproblem

        2. dp arr

        用 dp(i,j) 表示以(i,j) 为右下角，且只包含 1 的正方形的边长最大值。

        3. dp equation

        dp[i][j] = 1 + min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])

        T：O(mn)
        S：O(mn)
        """

        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        res = 0

        # 初始化
        dp = [[0]*n for _ in range(m)]

        # 第一行
        for j in range(n):
            if matrix[0][j] == '1':
                dp[0][j] = 1
                res = 1

        # 第一列
        for i in range(m):
            if matrix[i][0] == '1':
                dp[i][0] = 1
                res = 1

        # 其他
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                    res = max(res, dp[i][j])

        return res*res
