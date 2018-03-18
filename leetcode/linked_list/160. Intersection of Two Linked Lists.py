# coding=utf-8

"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3

begin to intersect at node c1.

Notes:

    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        p1 = headA
        p2 = headB
        count1 = count2 = 0
        while p1:
            count1 += 1
            p1 = p1.next
        while p2:
            count2 += 1
            p2 = p2.next

        if p1 != p2:  # 有交点时，两个链表是公共的
            return None

        p1 = headA
        p2 = headB

        diff = abs(count1 - count2)

        if count1 > count2:
            for _ in xrange(diff):
                p1 = p1.next
        else:
            for _ in xrange(diff):
                p2 = p2.next

        while p1 != p2:
            p1 = p1.next
            p2 = p2.next

        return p1


class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = headB if not p1 else p1.next
            p2 = headA if not p2 else p2.next
        return p1
