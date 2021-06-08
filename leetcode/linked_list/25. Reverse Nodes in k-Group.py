# coding=utf-8

"""

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

    Only constant extra memory is allowed.
    You may not alter the values in the list's nodes, only nodes itself may be changed.


"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode

        https://leetcode-cn.com/problems/reverse-nodes-in-k-group/solution/kge-yi-zu-fan-zhuan-lian-biao-by-powcai/

    时间复杂度: O(N)
    空间复杂度: O(1)

可以递归操作, 有两种情况：

    就是压根没有k个node，那么我们直接保持这个k-group不动返回head
    如果有k个node的话，那么我们先找到第k个node之后的递归结果 node = nxt，然后反转前面k个node，让反转结果的结尾 tail.next = nxt

    1->2->3->4->5

        """
        cur = head
        cnt = 0
        while cur and cnt != k:  # 往后最多走k步
            cur = cur.next
            cnt += 1
        if cnt == k:  # 如果当前 k-group 有 k 个node的话
            # 先找到第k个node之后的递归结果 node = nxt
            # 让反转结果的结尾 tail.next = nxt
            nxt = self.reverseKGroup(cur, k)
            while cnt > 0:  # 反转前面k个node
                tmp = head.next
                head.next = nxt
                nxt = head
                head = tmp
                cnt -= 1
            return nxt
        # 当前 k-group 压根没有k个node，那么我们直接保持这个k-group不动返回head
        return head
