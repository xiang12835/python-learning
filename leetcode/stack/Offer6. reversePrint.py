# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []

        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        r = []
        while stack:
            r.append(stack.pop())

        return r
