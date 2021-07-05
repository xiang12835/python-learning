# coding=utf-8


"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.


"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)

        return max(l, r) + 1



class Solution1:
    def maxDepth(self, root: TreeNode) -> int:
        """
        递归

        T: O(n)
        S: O(h)
        """
        if not root:
            return 0
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        if not l and not r:
            return 1
        elif not l:
            return r + 1
        elif not r:
            return l + 1
        else:
            return max(l, r) + 1
