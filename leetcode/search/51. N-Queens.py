# coding=utf-8

"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。

"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n < 1:
            return []

        self.result = []
        self.cols = set()
        self.pie = set()
        self.na = set()

        self.dfs(n, 0, [])

        return self.gen_result(n)

    def dfs(self, n, row, cur_state):
        # recursion terminator
        if row >= n:
            self.result.append(cur_state)
            return

        for col in range(n):
            if col in self.cols or row + col in self.pie or row - col in self.na:
                continue

            # update flags
            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)

            self.dfs(n, row + 1, cur_state + [col])

            # remove flags
            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)

    def gen_result(self, n):
        board = []
        for res in self.result:
            for i in res:
                board.append('.' * i + 'Q' + '.' * (n - 1 - i))

        return [board[i:i + n] for i in range(0, len(board), n)]



class Solution1:
    def solveNQueens(self, n):
        def dfs(queens, xy_diff, xy_sum):
            p = len(queens)
            if p == n:
                res.append(queens)
                return

            for q in range(n):
                if q not in queens and p-q not in xy_diff and p+q not in xy_sum:
                    dfs(queens + [q], xy_diff+[p-q], xy_sum+[p+q])

        res = []
        dfs([], [], [])
        return [['.' * i + 'Q' + '.' * (n-i-1) for i in sol] for sol in res]


if __name__ == "__main__":
    s = Solution1()
    print(s.solveNQueens(4))
