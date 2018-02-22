# coding=utf-8


"""问题描述

输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。

"""


"""思路解析

题目要求找到所有路径，经典的DFS
"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, Number):
        if root==None:
            return []
        if root.left==None and root.right==None and Number==root.val:
            return [[root.val]]
        if root.left==None and root.right==None and Number!=root.val:
            return []
        res=[]
         #进行递归
        res_left=self.FindPath(root.left,Number-root.val)
        res_right=self.FindPath(root.right,Number-root.val)
        for i in res_left+res_right:  # 取交集
            res.append([root.val]+i)
        return res