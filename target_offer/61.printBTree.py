# -*- coding:utf-8 -*-


"""题目描述

从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。

"""


"""思路解析
层次遍历
"""

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []

        r = []
        node_stack = [pRoot]
        while node_stack:
            val_list = []
            tmp_stack = []
            for node in node_stack:
                val_list.append(node.val)
                if node.left:
                    tmp_stack.append(node.left)
                if node.right:
                    tmp_stack.append(node.right)
            node_stack = tmp_stack
            r.append(val_list)
        return r
