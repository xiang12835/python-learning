# coding=utf-8


"""问题描述

输入一个链表，反转链表后，输出链表的所有元素。

"""


"""思路解析

从根节点开始，利用头插法将链表进行反转

"""


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return None

        pre = None
        cur = pHead
        while cur.next:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        cur.next = pre
        return cur

