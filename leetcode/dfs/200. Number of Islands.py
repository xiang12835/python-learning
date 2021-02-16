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


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        dfs

        T：O(MN)，其中 M 和 N 分别为行数和列数。
        S：O(MN)，在最坏情况下，整个网格均为陆地，深度优先搜索的深度达到 M*N。
        """
        # 检查参数
        count = 0
        m = len(grid)
        if m == 0:
            return 0

        n = len(grid[0])

        # 两层循环扫描，当发现是陆地时，将其周围相邻的岛屿都夷为平地
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j, m, n)
        return count

    def dfs(self, grid, i, j, m, n):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j, m, n)
        self.dfs(grid, i - 1, j, m, n)
        self.dfs(grid, i, j + 1, m, n)
        self.dfs(grid, i, j - 1, m, n)
