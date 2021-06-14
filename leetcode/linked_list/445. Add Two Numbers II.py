# coding=utf-8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        栈 + 头插法

        T: O(max(m,n))
        S: O(m + n)
        """
        dummy = ListNode(-1)
        stack1 = []
        stack2 = []

        def push_stack(p, stack):
            while p:
                stack.append(p.val)
                p = p.next

        push_stack(l1, stack1)  # l1 压栈
        push_stack(l2, stack2)  # l2 压栈

        carry = 0  # 记录进位
        while stack1 or stack2 or carry:
            tmp1, tmp2 = 0, 0
            if stack1:
                tmp1 = stack1.pop()
            if stack2:
                tmp2 = stack2.pop()

            data = (carry + tmp1 + tmp2) % 10
            carry = (carry + tmp1 + tmp2) // 10

            # 头插法
            cur = ListNode(data)
            cur.next = dummy.next
            dummy.next = cur

        return dummy.next