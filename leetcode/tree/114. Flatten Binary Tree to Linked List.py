# coding=utf-8


"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        ll = []

        def dfs(root):
            if not root:
                return
            ll.append(root)
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        for i in range(1, len(ll)):
            pre, cur = ll[i - 1], ll[i]
            pre.left = None
            pre.right = cur
