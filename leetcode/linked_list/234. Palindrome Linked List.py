"""
Given a singly linked list, determine if it is a palindrome.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
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

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        l1 = []
        p = head
        while p:
            l1.append(p.val)
            p = p.next

        reverse_head = self.reverseList(head)

        l2 = []
        p = reverse_head
        while p:
            l2.append(p.val)
            p = p.next

        return l1 == l2
