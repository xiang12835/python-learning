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



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        队列

        cur_level来记录当前层的数据
        cur_size 当前这一层的节点个数

        T：每个点进队出队各一次，故渐进时间复杂度为 O(n)。
        S：队列中元素的个数不超过 n 个，故渐进空间复杂度为 O(n)。
        """
        if not root:
            return []

        res = []
        queue = [root]
        while queue:
            # 获取当前队列的长度，这个长度相当于 当前这一层的节点个数
            cur_size = len(queue)
            cur_level = []
            # 将队列中的元素都拿出来(也就是获取这一层的节点)，放到临时list中
            # 如果节点的左/右子树不为空，也放入队列中
            for _ in range(cur_size):
                node = queue.pop(0)  # 易错
                cur_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(cur_level)

        return res
