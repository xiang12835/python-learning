# -*- coding:utf-8 -*-


"""题目描述

请实现两个函数，分别用来序列化和反序列化二叉树

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.idx = -1

    def Serialize(self, root):
        # write code here
        if not root:
            return '#,'
        return str(root.val) + ',' + self.Serialize(root.left) + self.Serialize(root.right)

    def Deserialize(self, s):
        # write code here
        self.idx += 1
        l = s.split(',')

        if self.idx >= len(s):
            return

        root = None
        if l[self.idx] != '#':
            root = TreeNode(int(l[self.idx]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root
