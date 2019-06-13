# coding=utf-8


"""问题描述

输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）

"""

"""思路解析

采用递归的思路，单独定义一个函数判断B是不是从当前A的根节点开始的子树，这里判断是不是子树也需要一个递归的判断。如果是，则返回True，如果不是，再判断B是不是从当前A的根节点的左子节点或右子节点开始的子树。

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # 判断根结点是否相等
        if not pRoot1 or not pRoot2:
            return False

        r = False
        if pRoot1.val == pRoot2.val:
            r = self.isSubTree(pRoot1, pRoot2)
        if not r:
            r = self.isSubTree(pRoot1.left, pRoot2)
        if not r:
            r = self.isSubTree(pRoot1.right, pRoot2)
        return r

    def isSubTree(self, pRoot1, pRoot2):
        # 判断子结点是否相等
        if not pRoot2:
            return True

        if not pRoot1:
            return False

        if pRoot1.val == pRoot2.val:
            return self.isSubTree(pRoot1.left, pRoot2.left) and self.isSubTree(pRoot1.right, pRoot2.right)

