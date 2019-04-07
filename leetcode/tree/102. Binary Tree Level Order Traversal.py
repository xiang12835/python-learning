# coding=utf-8


"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        利用cur_level来记录当前层的数据
        tmp_queue来存放待进入的队列

        """
        if not root:
            return []

        r, queue = [], [root]

        # visited = set()

        while queue:
            cur_size = len(queue)
            cur_level = []
            tmp_queue = []
            for i in xrange(cur_size):
                node = queue[i]
                cur_level.append(node.val)
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)

            queue = tmp_queue
            r.append(cur_level)

        return r
