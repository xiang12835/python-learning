# coding=utf-8

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int


        0 [7, 1, 8, 3]
        1 [7, 6, 8, 3]
        2 [7, 6, 10, 3]
        0 [9, 6, 10, 3]
        1 [9, 10, 10, 3]
        0 [11, 10, 10, 3]
        11

        """
        if not triangle:
            return 0

        res = triangle[-1]
        for i in xrange(len(triangle) - 2, -1, -1):
            for j in xrange(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]

                # print j, res
        return res[0]


class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        brute-force, 递归，n层：left or right: 2^n

        优化：记忆化搜索

        DP:
        a. 重复性（分治）：problem(i,j) = min(sub(i+1, j), sub(i+1,j+1)) + a(i,j)
        b. 定义状态数组: f[i,j]
        c. DP 方程: f[i,j] = min(f[i+1,j], f[i+1,j+1]) + a[i,j]

        由底向上
        """
        dp = triangle
        for i in range(len(dp) - 2, -1, -1):
            for j in range(len(dp[i])):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + dp[i][j]

        return dp[0][0]


if __name__ == "__main__":
    s = Solution()
    print s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])
