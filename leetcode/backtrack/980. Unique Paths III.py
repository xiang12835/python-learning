# coding=utf-8

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        self.res = 0
        sr, sc = 0, 0                     #起点，终点
        er, ec = 0, 0
        step = 0                        #非障碍的个数

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    sr, sc = r, c
                if grid[r][c] == 2:
                    er, ec = r, c
                if grid[r][c] != -1:
                    step += 1

        def backtrack(x, y, step):
            if not 0 <= x < m or not 0 <= y < n or not grid[x][y] != -1:
                return

            step -= 1
            if x == er and y == ec:
                if step == 0:
                    self.res += 1
                return

            grid[x][y] = -1

            backtrack(x-1, y, step)
            backtrack(x+1, y, step)
            backtrack(x, y-1, step)
            backtrack(x, y+1, step)

            grid[x][y] = 0 #回溯算法

        backtrack(sr, sc, step)

        return self.res



