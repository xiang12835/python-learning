# coding=utf-8

"""

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.



Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        递归
        """
        if not head or not head.next:
            return head
        tmp = head.next
        head.next = self.swapPairs(head.next.next)
        tmp.next = head
        return tmp


class Solution1:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        循环；哨兵

        1->2->3->4

        -1->2->1->4->3->null

        """
        if not head or not head.next:
            return head

        cur = dummy = ListNode(-1)
        dummy.next = head

        while cur.next and cur.next.next:
            next_one, next_two, next_three = cur.next, cur.next.next, cur.next.next.next
            cur.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            cur = next_one
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        迭代法

        T: O(N)
        S: O(1)
        """

        if not head or not head.next:
            return head # 易错

        dummy = cur = ListNode(-1)
        dummy.next = head # 易错，需要连接起来

        while cur.next and cur.next.next:
            one = cur.next
            two = cur.next.next
            tree = cur.next.next.next

            cur.next = two
            two.next = one
            one.next = tree

            cur = one

        return dummy.next