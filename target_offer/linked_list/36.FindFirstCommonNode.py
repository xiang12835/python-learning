# coding=utf-8


"""问题描述

输入两个链表，找出它们的第一个公共结点。


"""


"""思路解析

两个指针，一个先遍历链表1，再遍历链表2 一个先遍历链表2再遍历链表1

"""


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None

        p1 = pHead1
        p2 = pHead2
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

            if not p1 and not p2:
                return None

            if not p1:
                p1 = pHead2
            if not p2:
                p2 = pHead1

        return p1
