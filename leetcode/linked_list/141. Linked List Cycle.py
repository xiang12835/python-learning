# coding=utf-8

"""
 Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        slow = head
        fast = head.next
        while fast != slow:
            if not fast or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next

        return True


class Solution1(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool

        快慢指针
        """

        slow = head
        fast = head
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False
