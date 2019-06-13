# coding=utf-8

"""问题描述

从上往下打印出二叉树的每个节点，同层节点从左至右打印。

"""

"""思路解析
层次遍历的思路
"""

class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        queue = [root]
        r = []
        while queue:
            p = queue.pop(0)
            r.append(p.val)
            if p.left:
                queue.append(p.left)
            if p.right:
                queue.append(p.right)
        return r
