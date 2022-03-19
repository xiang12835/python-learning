"""
 Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1

return

[
   [5,4,11,2],
   [5,8,4,5]
]

"""

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        dfs

        T: O(N^2)
        S: O(N)
        """

        def dfs(node, sum, path):
            # 空节点，不处理
            if not node:
                return

                # 叶子节点
            if not node.left and not node.right:
                if node.val == sum:
                    res.append(path+[node.val])

            # 左子树
            dfs(node.left, sum-node.val, path+[node.val])

            # 右子树
            dfs(node.right, sum-node.val, path+[node.val])

        res = []
        dfs(root, targetSum, [])
        return res

