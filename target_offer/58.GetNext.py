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


# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None


class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode == None:
            return None

        if pNode.right:
            pNode = pNode.right
            while pNode:
                if pNode.left == None:
                    return pNode
                pNode = pNode.left

        while pNode:
            if pNode.next:
                if pNode.next.left == pNode:
                    return pNode.next
                else:
                    pNode = pNode.next
            else:
                break

