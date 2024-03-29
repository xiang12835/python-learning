# coding=utf-8

"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.



Follow up:
Can you solve it without using extra space?

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        快慢指针

        在 python 中，while … else 在循环条件为 false 时执行 else 语句块

        """
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow: # 双指针第一次相遇
                break
        else:
            return None

        while head != slow: # 双指针第二次相遇
            head = head.next
            slow = slow.next

        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution1:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow ==fast:
                break
        if not fast or not fast.next: # 易错
            return None
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return fast



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution2(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        快慢指针

        https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/

        """

        fast, slow = head, head
        while True:
            if not (fast and fast.next): # 不相交
                return
            fast, slow = fast.next.next, slow.next
            if fast == slow:  # 第一次相遇
                break
        fast = head
        while fast != slow: # 第二次相遇
            fast, slow = fast.next, slow.next
        return fast
