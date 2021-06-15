# coding=utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        递归

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        if not (preorder and inorder):
            return None
        # 根据前序数组的第一个元素，就可以确定根节点
        root = TreeNode(preorder[0])
        # 用preorder[0]去中序数组中查找对应的元素
        mid_idx = inorder.index(preorder[0])
        # 递归处理前序数组左边部分和中序数组左边部分
        root.left = self.buildTree(preorder[1:mid_idx + 1], inorder[:mid_idx])
        # 递归的处理前序数组的右边部分和中序数组的右边部分
        root.right = self.buildTree(preorder[mid_idx + 1:], inorder[mid_idx + 1:])
        return root
