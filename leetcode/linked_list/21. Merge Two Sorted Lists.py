# coding=utf-8
"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.nxt = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        迭代法 + 哨兵
        T: O(m+n)
        S: O(1)
        """
        head = tmp = Node(-1)

        while l1 and l2:
            if l1.val < l2.val:
                tmp.nxt = l1
                l1 = l1.nxt
            else:
                tmp.nxt = l2
                l2 = l2.nxt
            tmp = tmp.nxt

        if l1:
            tmp.nxt = l1
        if l2:
            tmp.nxt = l2

        return head.nxt
