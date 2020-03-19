# coding=utf-8

"""

Implement a function to check if a linked list is a palindrome.



Example 1:

Input:  1->2
Output:  false
Example 2:

Input:  1->2->2->1
Output:  true

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool

        要想实现O(1)的空间复杂度，
        可以找到中间的节点，把linked list拆成两个部分，
        后半部分linkedlist reverse，
        然后比较两个linked list值是否相同

        T: O(n)
        S: O(1)

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
        p = head
        while p and pre:
            if p.val != pre.val:
                return False

            p = p.next
            pre = pre.next

        return True
