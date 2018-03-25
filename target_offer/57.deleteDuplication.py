# coding=utf-8


# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if not pHead or not pHead.next:  # 只有0个或1个结点，则返回
            return pHead

        if pHead.val == pHead.next.val:  # 当前结点是重复结点
            p = pHead.next
            while p and p.val == pHead.val:  # 跳过值与当前结点相同的全部结点,找到第一个与当前结点不同的结点
                p = p.next
            return self.deleteDuplication(p)  # 从第一个与当前结点不同的结点开始递归
        else:  # 当前结点不是重复结点
            pHead.next = self.deleteDuplication(pHead.next)  # 保留当前结点，从下一个结点开始递归
            return pHead


if __name__ == "__main__":

    # {1,2,3,3,4,4,5}

    head = ListNode(1)

    node1 = ListNode(2)
    head.next = node1
    node2 = ListNode(3)
    node1.next = node2
    node3 = ListNode(3)
    node2.next = node3
    node4 = ListNode(4)
    node3.next = node4
    node5 = ListNode(4)
    node4.next = node5
    node6 = ListNode(5)
    node5.next = node6
    node6.next = None



    s = Solution()
    p = s.deleteDuplication(head)

    while p:
        print p.val
        p = p.next

