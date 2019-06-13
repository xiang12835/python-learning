# coding=utf-8


"""问题描述

输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

"""


"""思路解析

题目要求找到所有路径，经典的DFS
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root == None:
            return []

        if root.left == None and root.right == None and root.val != expectNumber:
            return []

        if root.left == None and root.right == None and root.val == expectNumber:
            return [[root.val]]

        r = []

        result_left = self.FindPath(root.left, expectNumber - root.val)
        result_right = self.FindPath(root.right, expectNumber - root.val)

        for v in result_left + result_right:
            r.append([root.val] + v)
        return r