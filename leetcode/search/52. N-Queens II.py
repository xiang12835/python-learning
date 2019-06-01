# coding=utf-8

"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return []
        self.count = 0
        self.dfs(n, 0, 0, 0, 0)
        return self.count

    def dfs(self, n, row, col, pie, na):
        # 递归终止条件
        if row >= n:
            self.count += 1
            return

        bits = (~(col | pie | na)) & ((1 << n) - 1)  # 得到当前所有的空位，‘1’的位置就是能填皇后的位置

        while bits:
            p = bits & -bits  # 取到最低位的1
            self.dfs(n, row + 1, col | p, (pie | p) << 1, (na | p) >> 1)
            bits = bits & (bits - 1)  # 去掉最低位的1

