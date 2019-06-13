# coding=utf-8


"""问题描述

输入一棵二叉树，判断该二叉树是否是平衡二叉树。


"""

"""思路解析

使用递归的思路求解二叉树的深度。定义一个新函数，用来求解二叉树的深度，如果左右子树的深度之差超过1，那么返回-1，代表不是平衡二叉树，否则，返回子树的深度。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True

        left_depth = self.TreeDepth(pRoot.left)
        right_depth = self.TreeDepth(pRoot.right)
        diff = left_depth - right_depth
        if diff > 1 or diff < -1:
            return False

        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0

        left_depth = self.TreeDepth(pRoot.left)
        right_depth = self.TreeDepth(pRoot.right)
        return max(left_depth, right_depth) + 1


class Solution1:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True

        left_depth = self.TreeDepth(pRoot.left)
        right_depth = self.TreeDepth(pRoot.right)
        if abs(left_depth - right_depth) > 1:
            return False

        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def TreeDepth(self, p):
        if not p:
            return 0

        left_res = self.TreeDepth(p.left)
        right_res = self.TreeDepth(p.right)

        return max(left_res, right_res) + 1

