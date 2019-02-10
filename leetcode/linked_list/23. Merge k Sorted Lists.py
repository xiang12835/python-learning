# coding=utf-8

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heappush, heappop
        nodes_pool = []
        dummy = cur = ListNode(-1)
        for head in lists:
            if head:
                heappush(nodes_pool, [head.val, head])
        while nodes_pool:
            smallest_node = heappop(nodes_pool)[1]
            cur.next = smallest_node
            cur = cur.next
            if smallest_node.next:
                heappush(nodes_pool, [smallest_node.next.val, smallest_node.next])
        return dummy.next


