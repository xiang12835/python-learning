# coding=utf-8

"""

判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(9):
            if not self.isValidList([board[i][j] for j in xrange(9)]) or \
               not self.isValidList([board[j][i] for j in xrange(9)]):
                return False
        for i in xrange(3):
            for j in xrange(3):
                if not self.isValidList([board[m][n] for n in xrange(3 * j, 3 * j + 3) \
                                                     for m in xrange(3 * i, 3 * i + 3)]):
                    return False
        return True

    def isValidList(self, xs):
        xs = filter(lambda x: x != '.', xs)
        return len(set(xs)) == len(xs)
