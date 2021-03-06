# coding=utf-8

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int

        dp[i][j] 是到达 i, j 最多路径
        动态方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]
        注意，对于第一行 dp[0][j]，或者第一列 dp[i][0]，由于都是在边界，所以只能为 1

        T：O(m*n)
        S：O(m*n)
        """
        dp = [[1]*n] + [[1] + [0]*(n-1) for _ in range(m-1)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
