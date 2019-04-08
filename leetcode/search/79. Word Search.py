# coding=utf-8

"""

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool

        超时

        """
        if not board:
            return False
        if not word:
            return True

        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.word = word

        self.row = len(board)
        self.col = len(board[0]) if self.row else 0

        ans_list = []
        for i in xrange(self.row):
            for j in xrange(self.col):
                if board[i][j] in self.word:
                    ans = self.dfs(board, i, j, 0)
                    ans_list.append(ans)
        return any(ans_list)

    def dfs(self, board, i, j, idx):

        if not 0 <= i < self.row or not 0 <= j < self.col or board[i][j] != self.word[idx]:
            return False

        if idx == len(self.word) - 1:
            return True

        board[i][j] = '@'
        res_list = []
        for k in xrange(4):
            x = i + self.dx[k]
            y = j + self.dy[k]

            res = self.dfs(board, x, y, idx+1)
            res_list.append(res)

        board[i][j] = self.word[idx]

        return any(res_list)


class Solution1(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool

        有问题

        """
        if not board:
            return False
        if not word:
            return True

        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]

        self.word_list = list(word)

        self.row = len(board)
        self.col = len(board[0]) if self.row else 0

        for i in xrange(self.row):
            for j in xrange(self.col):
                if board[i][j] in self.word_list:
                    self.dfs(board, i, j, '', self.word_list)

    def dfs(self, board, i, j, cur_word, cur_word_list):
        cur_word += board[i][j]
        cur_word_list = cur_word_list.remove(board[i][j])
        if not cur_word_list:
            return True

        tmp, board[i][j] = board[i][j], '@'
        for k in xrange(4):
            x = i + self.dx[k]
            y = j + self.dy[k]

            if 0 <= x < self.row and 0 <= y < self.col and board[x][y] != '@' and board[x][y] in cur_word_list:
                self.dfs(board, x, y, cur_word, cur_word_list)

        board[i][j] = tmp


class Solution3(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        if not word:
            return True

        row = len(board)
        col = len(board[0]) if row else 0

        def dfs(i, j, idx):
            if not 0 <= i < row or not 0 <= j < col or board[i][j] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            board[i][j] = '*'
            res = dfs(i + 1, j, idx + 1) or dfs(i, j + 1, idx + 1) or dfs(i - 1, j, idx + 1) or dfs(i, j - 1, idx + 1)
            board[i][j] = word[idx]
            return res

        return any(dfs(i, j, 0) for i in range(row) for j in range(col))
