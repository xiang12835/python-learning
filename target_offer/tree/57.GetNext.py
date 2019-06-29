# coding=utf-8


"""题目描述
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
"""


"""思路解析
分析二叉树的下一个节点，一共有以下情况：
1.二叉树为空，则返回空；
2.节点右孩子存在，则设置一个指针从该节点的右孩子出发，一直沿着指向左子结点的指针找到的叶子节点即为下一个节点；
3.没有右节点但有父节点，则判断当前节点是否为父节点的左节点，若不是循环搜索父节点的父节点，并重复判断；
"""


# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode:  # 二叉树为空，则返回空
            return

        if pNode.right:  # 节点右孩子存在
            pNode = pNode.right  # 设置一个指针从该节点的右孩子出发
            while pNode:  # 一直沿着指向左子结点的指针找到的叶子节点即为下一个节点
                if not pNode.left:  # 叶子节点
                    return pNode
                pNode = pNode.left

        while pNode:
            if pNode.next:  # 没有右节点但有父节点
                if pNode == pNode.next.left:  # 判断当前节点是否为父节点的左节点
                    return pNode.next
                else:
                    pNode = pNode.next  # 若不是循环搜索父节点的父节点
            else:
                break


class Solution1:
    def GetNext(self, pNode):
        # write code here
        root = pNode
        while root.next:
            root = root.next
        self.result = []
        self.midOrder(root)
        if self.result.index(pNode) != len(self.result) - 1:
            return self.result[self.result.index(pNode) + 1]
        else:
            return None

    def midOrder(self, root):
        if not root:
            return None
        self.midOrder(root.left)
        self.result.append(root)
        self.midOrder(root.right)
