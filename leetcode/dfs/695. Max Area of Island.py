#coding=utf-8

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        T：O(MN)
        S：O(MN)

        对于每一个点我们不停的dfs，然后每次碰到一个点是1我们就将当前area加1，然后把这个点变成0，每一次都更新我们的res，最终返回res
        """
        m = len(grid)
        if not m:
            return 0
        n = len(grid[0])

        def dfs(i, j, area):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] != 1:
                return area

            grid[i][j] = 0
            area += 1

            area = dfs(i-1, j, area)
            area = dfs(i+1, j, area)
            area = dfs(i, j-1, area)
            area = dfs(i, j+1, area)

            return area

        res = 0
        for i in range(m):
            for j in range(n):
                area = dfs(i, j, 0)
                res = max(res, area)

        return res
