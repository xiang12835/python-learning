#coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]

        T: O(N^2)
        S: O(N)
        """

        self.res = []
        self.dfs(root, targetSum, [])
        return self.res

    def dfs(self, node, sum, path):
        if not node: # 空节点，不做处理
            return

        if not node.left and not node.right: # 叶子结点
            if sum == node.val: # # 剩余的路径和恰好等于叶子节点值
                self.res.append(path + [node.val])  # 把该路径放入结果中

        self.dfs(node.left, sum - node.val, path + [node.val]) # 左子树
        self.dfs(node.right, sum - node.val, path + [node.val]) # 右子树

