# coding=utf-8


"""题目描述

请实现一个函数，用来判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。

"""


"""思路解析1

首先根节点以及其左右子树，左子树的左子树和右子树的右子树相同
左子树的右子树和右子树的左子树相同即可，采用递归

"""


"""思路解析2

非递归也可，采用栈或队列存取各级子树根节点

"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot:
            return True
        return self.compare(pRoot.left, pRoot.right)

    def compare(self, p1, p2):
        if not p1 and not p2:
            return True

        if p1.left and not p2.right:
            return False

        if not p1.left and p2.right:
            return False

        if p1.val == p2.val and self.compare(p1.left, p2.right) and self.compare(p1.right, p2.left):
            return True

