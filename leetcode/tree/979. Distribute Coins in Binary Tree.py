# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        """ 后序遍历
        https://leetcode-cn.com/problems/distribute-coins-in-binary-tree/solution/yi-tu-ding-suo-you-chang-gui-ti-by-xiao-cmmll/

        过载量 = Math.abs(num_coins - 1)

        定义 dfs(node) 为这个节点所在的子树中金币的过载量，也就是这个子树中金币的数量减去这个子树中节点的数量

        节点金币的过载量为 node.val + dfs(node.left) + dfs(node.right) - 1。

        T: O(N)
        S: O(H)
        """
        self.res = 0

        # 后序遍历，计算使每个结点上只有一枚硬币所需的移动次数
        def dfs(node):
            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)
            self.res += abs(l) + abs(r)  # 左右子树移动次数

            return node.val + l + r - 1 # 节点金币的过载量

        dfs(root)
        return self.res
