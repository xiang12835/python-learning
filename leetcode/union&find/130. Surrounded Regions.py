# coding=utf-8

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        dfs

        T: O(mn)
        S: O(mn)
        """

        if not board:
            return

        m = len(board)
        n = len(board[0])

        # 对于每一个边界上的 O，我们以它为起点，标记所有与它直接或间接相连的字母 O
        def dfs(x, y):
            if not 0 <= x < m or not 0 <= y < n or board[x][y] != "O":
                return
            board[x][y] = "#"
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)

        # 边界 - 列
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        # 边界 - 行
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        # 修改
        for i in range(m):
            for j in range(n):
                if board[i][j] == "#":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
