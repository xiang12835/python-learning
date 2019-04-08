# coding=utf-8

"""

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example:

Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]


Note:

All inputs are consist of lowercase letters a-z.
The values of words are distinct.

"""


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        if not words:
            return []

        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.end_of_word = '#'

        self.result = set()

        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[self.end_of_word] = self.end_of_word

        self.row, self.col = len(board), len(board[0])

        for i in xrange(self.row):
            for j in xrange(self.col):
                if board[i][j] in root:
                    self.dfs(board, i, j, '', root)

        return list(self.result)

    def dfs(self, board, i, j, cur_word, cur_dict):
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]

        if self.end_of_word in cur_dict:
            self.result.add(cur_word)

        tmp, board[i][j] = board[i][j], '@'
        for k in xrange(4):
            x, y = i + self.dx[k], j + self.dy[k]
            if 0 <= x < self.row and 0 <= y < self.col and board[x][y] != '@' and board[x][y] in cur_dict:
                self.dfs(board, x, y, cur_word, cur_dict)
        board[i][j] = tmp
