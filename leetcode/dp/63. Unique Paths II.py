# coding=utf-8

"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = 1
        for j in range(1, n):
            if obstacleGrid[0][j] == 0:  # 第一行无障碍（obstacleGrid[0][j] == 0）变为1
                dp[0][j] = dp[0][j-1]

        for i in range(1, m):
            if obstacleGrid[i][0] == 0:  # 第一列无障碍（obstacleGrid[i][0] == 0）变为1
                dp[i][0] = dp[i-1][0]

        print dp

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:  # 无障碍
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    dp[i][j] = 0
        return dp[-1][-1]


if __name__ == "__main__":
    # print Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
    # print Solution().uniquePathsWithObstacles([[1,0]])
    print Solution().uniquePathsWithObstacles([[0,0],[1,1],[0,0]])
