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


class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        回溯 + 剪枝

        x: 递归的深度
        y: 枚举每一列的位置，检查能否放皇后

        写一个DFS，按照每一层（x）进行遍历，在当前层去循环每一列（y）的位置

        时间复杂度：O(N!)
        空间复杂度：O(N)
        """
        self.res = 0

        def backtrack(cols, xy_diff, xy_sum):
            x = len(cols)
            if x == n:
                self.res += 1
                return

            for y in range(n):
                if y not in cols and x-y not in xy_diff and x+y not in xy_sum:
                    backtrack(cols+[y], xy_diff+[x-y], xy_sum+[x+y])

        backtrack([], [], [])

        return self.res


class Solution1(object):
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


if __name__ == "__main__":
    s = Solution()
    print(s.totalNQueens(4))

