# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.nxt = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = tmp = ListNode(-1)

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
