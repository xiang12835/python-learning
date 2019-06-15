# coding=utf-8


"""问题描述

输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。

"""


"""思路解析

递归进行判断，如果序列的长度小于等于2，那么一定是后序遍历的结果，否则根据BST和后序遍历的性质，遍历结果的最后一个一定是根节点，那么序列中前面一部分小于根节点的数是左子树，后面一部分是右子树，递归进行判断。

"""


class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False

        n = len(sequence)
        root = sequence[n - 1]

        # 在二叉搜索树中左子树节点小于根节点
        idx = 0
        while sequence[idx] < root:
            idx += 1

        # 二叉搜索树中右子树的节点都大于根节点
        for j in xrange(idx, n):
            if sequence[j] < root:
                return False

        # 判断左子树是否为二叉树
        left = True
        if idx > 0:
            left = self.VerifySquenceOfBST(sequence[:idx])

        # 判断右子树是否为二叉树
        right = True
        if idx < n - 1:
            right = self.VerifySquenceOfBST(sequence[idx:-1])

        return left and right


if __name__ == "__main__":
    s = Solution()
    l = [5, 7, 6, 9, 11, 10, 8]
    print s.VerifySquenceOfBST(l)
