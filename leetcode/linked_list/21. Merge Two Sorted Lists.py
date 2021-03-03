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


class Solution1(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        迭代法 + 哨兵
        T: O(m+n)
        S: O(1)
        """
        head = cur = Node(0)

        while l1 and l2:
            if l1.val < l2.val:
                cur.nxt = l1
                l1 = l1.nxt
            else:
                cur.nxt = l2
                l2 = l2.nxt
            cur = cur.nxt

        if l1:
            cur.nxt = l1
        if l2:
            cur.nxt = l2

        return head.nxt


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        法二：递归
        两个链表头部值较小的一个节点与剩下元素的 merge 操作结果合并。
        T: O(m+n)
        S: O(m+n)
        """

        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
