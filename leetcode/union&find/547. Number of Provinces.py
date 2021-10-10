# coding=utf-8

class Solution1:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """ DFS
        T：O(n^2)，其中 n 是城市的数量。需要遍历矩阵 n 中的每个元素。
        S：O(n)，其中 n 是城市的数量。需要使用数组 visited 记录每个城市是否被访问过，数组长度是 n，递归调用栈的深度不会超过 n。
        """

        n = len(isConnected)
        visited = set()

        def dfs(i):
            for j in range(n):
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count

