# coding=utf-8

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
        if not self.is_valid(x, y):
            return 0

        self.visited.add((x, y))

        for k in xrange(4):
            self.dfs(x + self.dx[k], y + self.dy[k])

        return 1

    def is_valid(self, x, y):
        return 0 <= x < self.max_x and 0 <= y < self.max_y and self.grid[x][y] == '1' and (x, y) not in self.visited

