# coding=utf-8

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in xrange(9):
            if not self.is_valid([board[i][j] for j in xrange(9)]) or not self.is_valid(
                    [board[j][i] for j in xrange(9)]):
                return False

        for i in xrange(3):
            for j in xrange(3):
                if not self.is_valid([board[m][n] for n in xrange(3 * j, 3 * j + 3) for m in xrange(3 * i, 3 * i + 3)]):
                    return False

        return True

    def is_valid(self, datas):
        datas = filter(lambda x: x != '.', datas)
        return len(set(datas)) == len(datas)