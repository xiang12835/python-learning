# coding=utf-8

"""
Write code to remove duplicates from an unsorted linked list.

Example1:

 Input: [1, 2, 3, 3, 2, 1]
 Output: [1, 2, 3]
Example2:

 Input: [1, 1, 1, 1, 2]
 Output: [1, 2]

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        哨兵
        """
        if not head:
            return head

        ss = set()
        ss.add(head.val)

        dummy = ListNode(-1)
        dummy.next = head
        cur = head

        while cur and cur.next:
            if cur.next.val in ss:
                cur.next = cur.next.next
            else:
                ss.add(cur.next.val)
                cur = cur.next

        return dummy.next
