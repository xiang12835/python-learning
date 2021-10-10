# coding=utf-8

"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""


class Solution(object):
    def __init__(self):
        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0

        self.grid = grid
        self.max_x = len(grid)
        self.max_y = len(grid[0])
        self.visited = set()

        l = [self.dfs(i, j) for i in xrange(self.max_x) for j in xrange(self.max_y)]

        return sum(l)

    def dfs(self, x, y):
        if 0 <= x < self.max_x and 0 <= y < self.max_y and self.grid[x][y] == '1' and (x, y) not in self.visited:

            self.visited.add((x, y))

            for k in xrange(4):
                self.dfs(x + self.dx[k], y + self.dy[k])

            return 1

        return 0


class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        dfs

        T：O(MN)，其中 M 和 N 分别为行数和列数。
        S：O(MN)，在最坏情况下，整个网格均为陆地，深度优先搜索的深度达到 M*N。
        """
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])

        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] != "1":
                return
            grid[i][j] = '0'  # 将岛屿都夷为平地
            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)

        # 两层循环扫描，当发现是陆地时，将其周围相邻的岛屿都夷为平地
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count