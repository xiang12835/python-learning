# coding=utf-8


"""问题描述

输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。


"""

"""思路解析

使用递归的思路实现。

"""


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0

        left_depth = self.TreeDepth(pRoot.left)
        right_depth = self.TreeDepth(pRoot.right)
        return max(left_depth, right_depth) + 1
