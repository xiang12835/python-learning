# -*- coding:utf-8 -*-

"""
输入一个链表，从尾到头打印链表每个节点的值。

"""


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # 法一：从头到尾遍历链表，并用一个栈存储每个结点的值，之后出栈输出值即可
        if listNode == None:
            return
        l = []
        while listNode:
            l.insert(0, listNode.val)
            listNode = listNode.next
        return l

    def printListFromTailToHead2(self, listNode):
        if listNode == None:
            return
        l = []
        while listNode:
            l.append(listNode.val)
            listNode = listNode.next
        return l[::-1]


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

singleNode = ListNode(12)

test = ListNode()

S = Solution()
print(S.printListFromTailToHead(node1))
print(S.printListFromTailToHead(test))
print(S.printListFromTailToHead(singleNode))
