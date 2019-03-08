#coding=utf-8

"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.


"""


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        对于每一个点我们不停的dfs，然后每次碰到一个点是1我们就将当前area加1，然后把这个点变成0，每一次都更新我们的res，最终返回res
        """
        if not grid or len(grid) == 0:
            return 0

        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0]) if self.m else 0

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = self.dfs(i, j, 0)
                res = max(res, area)
        return res

    def dfs(self, i, j, area):
        if i < 0 or i >= self.m or j < 0 or j >= self.n or self.grid[i][j] != 1:
            return area
        else:
            self.grid[i][j] = 0
            area += 1
        for x, y in ([(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]):
            area = self.dfs(x, y, area)
        return area


class Solution1(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0]) if m else 0

        def dfs(i, j, area):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return area
            else:
                grid[i][j] = 0
                area += 1
            for x, y in ([(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]):
                area = dfs(x, y, area)
            return area

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = dfs(i, j, 0)
                res = max(res, area)
        return res