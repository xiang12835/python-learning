"""
Reverse a singly linked list.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        pre = None
        cur = head
        while cur.next:
            nxt = cur.next
            cur.next = pre

            pre = cur
            cur = nxt

        cur.next = pre

        return cur


class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre

            pre = cur
            cur = nxt

        return pre


class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self._reverse(head)

    def _reverse(self, node, pre=None):
        if not node:
            return pre
        nxt = node.next
        node.next = pre
        return self._reverse(nxt, node)
