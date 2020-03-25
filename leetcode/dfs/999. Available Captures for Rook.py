# coding=utf-8

"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.
"""


class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        self.ans = 0
        def dfs(i, j, dx, dy):
            if i < 0 or i >= 8 or j < 0 or j >= 8: return
            if board[i][j] == 'B': return
            if board[i][j] == 'p':
                self.ans += 1
                return
            dfs(i + dx, j + dy, dx, dy)

        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    dfs(i + 1, j, 1, 0)
                    dfs(i - 1, j, -1, 0)
                    dfs(i, j + 1, 0, 1)
                    dfs(i, j - 1, 0, -1)
        return self.ans