# coding=utf-8

"""

Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.


Example 1:

Given tree [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
return true.
Example 2:

Given [1,2,2,3,3,null,null,4,4]
      1
     / \
    2   2
   / \
  3   3
 / \
4   4
return false.

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def depth(root):
            if not root:
                return 0
            return 1 + max(depth(root.left), depth(root.right))

        if not root:
            return True

        if abs(depth(root.left) - depth(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
