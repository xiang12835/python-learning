# coding=utf-8

"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int


        递归

        时间复杂度：我们访问每个节点一次，时间复杂度为 O(N)，其中 N 是节点个数。
        空间复杂度：最坏情况下，整棵树是非平衡的，例如每个节点都只有一个孩子，递归会调用 N（树的高度）次，因此栈的空间开销是 O(N) 。但在最好情况下，树是完全平衡的，高度只有 log(N)，因此在这种情况下空间复杂度只有 O(log(N)) 。

        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if not left and not right:
            return 1
        elif not left:
            return right + 1
        elif not right:
            return left + 1
        else:
            return min(right, left) + 1

