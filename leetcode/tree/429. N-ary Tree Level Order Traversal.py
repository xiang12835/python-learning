# coding=utf-8

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        """
        队列

        T: O(n)
        S: O(n)
        """

        if not root:
            return

        res = []
        queue = [root]
        while queue:
            cur = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                cur.append(node.val)
                queue.extend(node.children)
            res.append(cur)
        return res
