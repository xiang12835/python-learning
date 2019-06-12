# coding=utf-8

"""题目描述

输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

"""


class Solution:
    # 返回合并后列表
    # 递归
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2

        if not pHead2:
            return pHead1

        if pHead1.val < pHead2.val:
            p = pHead1
            p.next = self.Merge(pHead1.next, pHead2)
        else:
            p = pHead2
            p.next = self.Merge(pHead1, pHead2.next)
        return p


class Solution1:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2

        if not pHead2:
            return pHead1

        # 头节点
        if pHead1.val < pHead2.val:
            p = pHead1
        else:
            p = pHead2

        # 比较
        p1 = pHead1.next
        p2 = pHead2.next
        if p1.val < p2.val:
            p.next = p1
            p1 = p1.next
        else:
            p.next = p2
            p2 = p2.next

        # 剩余节点
        if p1:
            p.next = p1
        else:
            p.next = p2

        return p
