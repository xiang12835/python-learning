# coding=utf-8


"""题目描述

请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推

"""


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []

        node_stack = [pRoot]
        l = []
        while node_stack:
            val_list = []
            tmp_stack = []
            for node in node_stack:
                val_list.append(node.val)
                if node.left:
                    tmp_stack.append(node.left)
                if node.right:
                    tmp_stack.append(node.right)
            l.append(val_list)
            node_stack = tmp_stack

        r = []
        for i, v in enumerate(l):
            if i % 2 == 0:
                r.append(v)
            else:
                r.append(v[::-1])
        return r