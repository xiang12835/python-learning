# coding=utf-8

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


class Solution1(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool

        直接把List中元素拷贝到数组中直接比较

        """
        _list = []
        p = head
        while p:
            _list.append(p.val)
            p = p.next

        return _list[::-1] == _list


class Solution2(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool

        要想实现O(1)的空间复杂度，
        可以找到中间的节点，把linked list拆成两个部分，
        后半部分linkedlist reverse，
        然后比较两个linked list值是否相同

        """
        # 找到中间节点
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # 翻转后半部分
        pre = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        # 比较前后两部分
        while head and pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next

        return True
