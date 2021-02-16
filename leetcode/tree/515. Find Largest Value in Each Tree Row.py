# coding=utf-8


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        """
        bfs（队列）

        T： O(N)，遍历树中所有节点。
        S： DFS 是 O(Height)，为树的高度，最好完全二叉树 O(log(N))，最坏链表 O(N)；BFS 就是某层最大节点个数。

        """
        if not root:
            return []

        res = []
        queue = []

        while queue:
            cur_size = len(queue)
            cur_level = []

            for _ in range(cur_size):
                node = queue.pop(0)
                cur_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            max_val = max(cur_level)
            res.append(max_val)

        return res
