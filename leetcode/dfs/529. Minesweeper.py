# coding=utf-8


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        # 定义 8 个方位
        dx = [-1, -1, -1, 0, 1, 1, 1, 0]
        dy = [-1, 0, 1, 1, 1, 0, -1, -1]

        m = len(board)
        n = len(board[0])

        def in_board(x, y):
            """判断坐标是否在限定边界内
            """
            return 0 <= x < m and 0 <= y < n

        def dfs(x, y):
            count = 0
            # 先判断相邻(8 个方位)的方块是否含有***
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                # 如果相邻方块都在限定范围内，且含有***，统计***数
                if in_board(nx, ny) and board[nx][ny] == 'M':
                    count += 1
            if count > 0:
                # 含有***，修改当前点为数字对应***数，返回
                board[x][y] = str(count)
                return
            # 如果相邻方块不含***，修改为 'B'
            # 并向相邻位置扩散搜索
            board[x][y] = 'B'
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if in_board(nx, ny) and board[nx][ny] == 'E':
                    dfs(nx, ny)

        x, y = click

        # 如果当前点击的是未挖出的***，那么将其修改为 'X'，返回
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            # 当点击的是未挖出的方块，分情况讨论
            dfs(x, y)

        return board
