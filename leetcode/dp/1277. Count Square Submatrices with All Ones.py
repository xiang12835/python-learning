class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
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

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                elif matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
                res += dp[i][j]

        return res
