# coding=utf-8


"""问题描述

操作给定的二叉树，将其变换为源二叉树的镜像。
输入描述:
二叉树的镜像定义：源二叉树
     8
    / \
   6  10
 / \ / \
5 7 9 11
镜像二叉树
    8
   / \
  10 6
 / \ / \
11 9 7 5


"""

"""思路解析
利用递归的思路,每次对换传入的根节点的左右子树即可。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 递归
    def Mirror(self, root):
        # write code here
        if not root:
            return None

        p = root
        tmp = p.left
        p.left = p.right
        p.right = tmp

        if p.left:
            self.Mirror(p.left)
        if p.right:
            self.Mirror(p.right)

