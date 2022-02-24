"""
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.res = 0
        self.helper(root, sum)
        return self.res

    def dfs(self, root, sum, count, res):
        if not root:
            return
        count += root.val
        if count == sum:
            self.res += 1
        self.dfs(root.left, sum, count, self.res)
        self.dfs(root.right, sum, count, self.res)

    def helper(self, root, sum):
        if not root:
            return
        self.dfs(root, sum, 0, self.res)
        self.helper(root.left, sum)
        self.helper(root.right, sum)


class Solution1:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        """ dfs

        我们首先想到的解法是穷举所有的可能，我们访问每一个节点 node，检测以 node 为起始节点且向下延深的路径有多少种。
        我们递归遍历每一个节点的所有可能的路径，然后将这些路径数目加起来即为返回结果。

        T: O(N^2)
        S: O(N)
        """
        def dfs(root, targetSum):
            if root is None:
                return 0

            ret = 0
            if root.val == targetSum:
                ret += 1

            ret += dfs(root.left, targetSum - root.val)
            ret += dfs(root.right, targetSum - root.val)
            return ret

        if root is None:
            return 0

        ret = dfs(root, targetSum)
        ret += self.pathSum(root.left, targetSum)
        ret += self.pathSum(root.right, targetSum)
        return ret