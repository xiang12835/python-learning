# coding=utf-8

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        先在找root的左子树的最近公共祖先得到返回值left， 再从右子树中查找最近公共祖先得到返回值right。

        若left为NULL，因为题目保证有解，所以答案必在右边
        若left不为NULL，则看right是否为NULL，若right为NULL， 则答案一定是左边这个left。
        若左右都不为NULL， 说明root在中间，p和q在两边。该根结点一定是最近公共祖先。

        https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/solution/mian-shi-ti-68-ii-er-cha-shu-de-zui-jin-gong-gon-7/

        """
        if not root or p == root or q == root:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if not l:
            return r
        if not r:
            return l
        return root

