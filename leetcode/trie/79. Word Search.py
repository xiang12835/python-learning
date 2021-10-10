# coding=utf-8


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if not m:
            return False

        n = len(board[0])

        # 当前位置为(i, j)，匹配到第k个字符
        def dfs(i, j, k):
            # terminater
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]:
                return False

            # process
            if k == len(word) - 1:
                return True

            board[i][j] = "@"  # 避免走回头路

            # drill down 上下左右四个方向进行搜索
            res = dfs(i - 1, j, k + 1) or dfs(i + 1, j, k + 1) or dfs(i, j - 1, k + 1) or dfs(i, j + 1, k + 1)

            # reverse
            board[i][j] = word[k]  # 恢复当前的网格内字符

            return res

        # 检查是否匹配
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
