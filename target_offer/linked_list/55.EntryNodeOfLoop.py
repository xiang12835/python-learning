# -*- coding:utf-8 -*-

"""题目描述

一个链表中包含环，请找出该链表的环的入口结点。

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead == None or pHead.next == None or pHead.next.next == None:
            return None
        fast = pHead.next.next
        slow = pHead.next
        while fast != slow:
            if fast.next == None or fast.next.next == None:
                return None
            fast = fast.next.next
            slow = slow.next

        fast = pHead
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast