# -*- coding:utf-8 -*-


"""题目描述

给定一颗二叉搜索树，请找出其中的第k大的结点。例如， 5 / \ 3 7 /\ /\ 2 4 6 8 中，按结点数值大小顺序第三个结点的值为4。

"""


"""思路解析
二叉搜索树(二叉排序树)的中序遍历有序
"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.r = []

    def KthNode(self, pRoot, k):
        # write code here
        if pRoot == None or k == 0:
            return None

        self.in_order(pRoot)

        if k > len(self.r):
            return None
        else:
            return self.r[k - 1]

    def in_order(self, pRoot):
        if pRoot == None:
            return None
        self.in_order(pRoot.left)
        self.r.append(pRoot)
        self.in_order(pRoot.right)
