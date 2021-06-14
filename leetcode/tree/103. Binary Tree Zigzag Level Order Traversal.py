# coding=utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ans = []
        queue = [root]
        level = 1

        while queue:
            cur_data = []
            cur_size = len(queue)
            for _ in range(cur_size):
                node = queue.pop(0)

                if level % 2 == 1:
                    cur_data.append(node.val)  # 尾插
                else:
                    cur_data.insert(0, node.val)  # 头插

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(cur_data)
            level += 1

        return ans