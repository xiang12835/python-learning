# coding=utf-8

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """
        回溯
        """

        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])

        self.res = 0

        sx, sy = 0, 0 # 起始位置
        ex, ey = 0, 0 # 结束位置
        step = 0 # 非障碍物

        # 找位置
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    sx = i
                    sy = j
                if grid[i][j] == 2:
                    ex = i
                    ey = j

                if grid[i][j] != -1:
                    step += 1

        # 函数：四个方向回溯
        def backtrack(x, y, step):
            if not 0 <= x < m or not 0 <= y < n or grid[x][y] == -1:
                return

            step -= 1
            if x == ex and y == ey:
                if step == 0:
                    self.res += 1
                return

            grid[x][y] = -1

            backtrack(x-1, y, step)
            backtrack(x+1, y, step)
            backtrack(x, y-1, step)
            backtrack(x, y+1, step)

            grid[x][y] = 0

        # 开始查找不同路径的数目
        backtrack(sx, sy, step)

        return self.res