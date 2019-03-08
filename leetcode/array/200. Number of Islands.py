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
        if not self.is_valid(x, y):
            return 0

        self.visited.add((x, y))

        for k in xrange(4):
            self.dfs(x + self.dx[k], y + self.dy[k])

        return 1

    def is_valid(self, x, y):
        if x < 0 or x >= self.max_x or y < 0 or y >= self.max_y:
            return False

        if self.grid[x][y] == '0' or ((x, y) in self.visited):
            return False

        return True


class Solution1(object):
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
