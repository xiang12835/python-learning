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
        n 是所有链表中元素的总和，k 是链表个数。

        法一：暴力，两两合并，O(KN)

        自顶向下的编程思想

        [[],[1]] 过不了
        """
        if not lists:
            return

        size = len(lists)
        ans = lists[0]
        for i in range(1, size):
            self.mergeTwoLists(ans, lists[i])

        return ans

    def mergeTwoLists(self, l1, l2):
        """
        法一：迭代法 + 哨兵
        T: O(m+n)
        S: O(1)
        """
        dummy = tmp = ListNode(-1)
        while l1 and l2:
            if l1.val <= l2.val: # 为什么要有等于号？
                tmp.next = l1
                l1 = l1.next
            else:
                tmp.next = l2
                l2 = l2.next
            tmp = tmp.next

        if l1:
            tmp.next = l1
        if l2:
            tmp.next = l2

        return dummy.next


class Solution1(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        n 是所有链表中元素的总和，k 是链表个数。

        法二：类似归并排序/快排：分治 O(NlogK)
        """




class Solution2(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode

        法三：堆、优先队列 O(NlogK)

        哨兵；小顶堆
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
            if smallest_node.next:  # 将最小节点链表的下一个节点进堆
                heappush(nodes_pool, [smallest_node.next.val, smallest_node.next])
        return dummy.next


