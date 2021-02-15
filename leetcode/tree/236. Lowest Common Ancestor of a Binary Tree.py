# coding=utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        递归

        时间复杂度：O(N)
        空间复杂度：O(N)
        """
        if not root:
            return root
        # 边界条件，如果匹配到left或right就直接返回停止递归
        if p == root or q == root:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        # 如果既在左子树找到，又在右子树找到，那么毫无疑问当前root就是公共节点
        if l and r:
            return root
        elif l:  # 只有左子树有，那么直接返回左子树匹配到的第一个节点
            return l
        else:
            return r
