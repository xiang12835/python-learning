# coding=utf-8


""" 题目描述

输入一个链表，输出该链表中倒数第k个结点。

"""

""" 思路解析
假设链表中的节点数大于等于k个，那么一定会存在倒数第k个节点，那么我们首先使用一个快指针往前走k步，然后使用一个慢指针随快指针一起每次往前走一步，两个指针之间始终有k的距离，当快指针走到末尾变为Null时，慢指针所在的位置就是倒数第k个节点。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head:
            return None
        p = head
        count = 0
        while p:
            count += 1
            p = p.next
        if k > count:
            return None
        p = head
        for _ in xrange(count-k):
            p = p.next
        return p


class Solution1:
    def FindKthToTail(self, head, k):
        # write code here
        if not head:
            return None
        first = head
        count = 0
        while first and count < k:
            count += 1
            first = first.next
        if k > count:
            return None

        second = head
        while first:
            first = first.next
            second = second.next
        return second
