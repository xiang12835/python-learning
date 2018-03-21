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
        while cur.next:
            nxt = cur.next
            cur.next = pre

            pre = cur
            cur = nxt

        cur.next = pre

        return cur

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        reverse_head = self.reverseList(head)

        p1 = head
        p2 = reverse_head

        while p1 and p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True
