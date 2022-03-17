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

        cur_word：现在整个单词已经组装到什么位置了
        cur_dict：剩余层级的字典树

        """
        if not board or not board[0]:
            return []
        if not words:
            return []

        self.dx = [-1, 1, 0, 0]
        self.dy = [0, 0, -1, 1]
        self.end_of_word = '#'

        self.result = set()

        # 构建 words 的字典树
        root = {}
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[self.end_of_word] = self.end_of_word

        # 搜索
        self.row, self.col = len(board), len(board[0])

        for i in range(self.row):
            for j in range(self.col):
                if board[i][j] in root:
                    self.backtrack(board, i, j, '', root)

        return list(self.result)

    def backtrack(self, board, i, j, cur_word, cur_dict):

        print(cur_dict)
        cur_word += board[i][j]
        cur_dict = cur_dict[board[i][j]]

        if self.end_of_word in cur_dict:
            self.result.add(cur_word)

        tmp, board[i][j] = board[i][j], '@'
        for k in range(4): # 4个方向
            x, y = i + self.dx[k], j + self.dy[k]
            if 0 <= x < self.row and 0 <= y < self.col and board[x][y] != '@' and board[x][y] in cur_dict:
                self.backtrack(board, x, y, cur_word, cur_dict)
        board[i][j] = tmp



class Solution1:
    def findWords(self, board, words):
        """
        cur_word：现在整个单词已经组装到什么位置了
        cur_dict：剩余层级的字典树
        """
        if not board:
            return []

        m = len(board)
        n = len(board[0])
        res = set()

        # 构建 words 的字典树
        root = {}
        end_of_word = "#"
        for word in words:
            node = root
            for c in word:
                node = node.setdefault(c, {})
            node[end_of_word] = end_of_word

        # 四方向搜索函数
        def dfs(i, j, cur_word, cur_dict):
            # terminator
            if not 0 <= i < m or not 0 <= j < n or board[i][j] not in cur_dict or board[i][j] == '*':
                return

            # process
            cur_word += board[i][j]
            cur_dict = cur_dict[board[i][j]]
            if end_of_word in cur_dict:
                res.add(cur_word)
            tmp = board[i][j]
            board[i][j] = '*' # 同一个单元格内的字母在一个单词中不允许被重复使用

            # drill
            dfs(i-1, j, cur_word, cur_dict)
            dfs(i+1, j, cur_word, cur_dict)
            dfs(i, j-1, cur_word, cur_dict)
            dfs(i, j+1, cur_word, cur_dict)

            # reverse if
            board[i][j] = tmp

        # 查找单词
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(i, j, '', root)

        return list(res)


if __name__ == "__main__":
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]

    s = Solution1()
    ans = s.findWords(board, words)
    print(ans)
