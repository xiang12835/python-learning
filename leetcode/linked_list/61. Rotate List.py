# coding=utf-8

"""

Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL


"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode

        反转三次链表
        """
        if not head or k == 0:
            return head

        tmp = head
        size = 0
        while tmp:
            tmp = tmp.next
            size += 1

        if k > size:
            k = k % size

        if k == 0:
            return head

        reverse_head = self._reverse(head)
        # 5->4->3->2->1

        dummy = ListNode(-1)
        dummy.next = reverse_head

        while k:
            dummy = dummy.next  # dummy:4
            k -= 1

        tmp_head = dummy.next  # tmp_head:3
        dummy.next = None

        reverse_head_one = self._reverse(reverse_head)
        # 4->5
        reverse_head_two = self._reverse(tmp_head)
        # 1->2->3

        cur = reverse_head_one

        while cur.next:
            cur = cur.next

        cur.next = reverse_head_two

        return reverse_head_one

    def _reverse(self, cur, pre=None):
        if not cur:
            return pre

        cur.next, pre, cur = pre, cur, cur.next

        head = self._reverse(cur, pre)

        return head


class Solution1:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
时间复杂度: O(N)
空间复杂度: O(N)
        """
        if not head or k == 0:
            return head

        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        k = k % len(nodes)
        if k == 0:
            return nodes[0]

        nodes[-k-1].next = None
        nodes[-1].next = nodes[0]
        return nodes[-k]


class Solution2:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL

时间复杂度: O(N)
空间复杂度: O(1)

        """
        if not head or k == 0:
            return head
        size = 0
        cur = tail = head
        while cur:
            size += 1
            tail = cur  # 5
            cur = cur.next

        k = k % size
        if k == 0:
            return head

        tmp = self.findLastKth(head, k, size)  # tmp:3
        last_kth = tmp.next  # last_kth:4
        tmp.next = None
        tail.next = head
        return last_kth

    def findLastKth(self, node, k, size):
        for i in range(size - k - 1):
            node = node.next
        return node


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution3:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        https://leetcode-cn.com/problems/rotate-list/solution/fu-xue-ming-zhu-wen-ti-chai-fen-fen-xian-z4dr/

        题意：将链表每个节点向右移动 k 个位置，相当于把链表的后面 k % len 个节点移到链表的最前面。（len 为 链表长度）

        所以本题的步骤：

        1. 求链表长度；
        2. 找出倒数第 k+1 个节点；
        3. 链表重整：将链表的倒数第 k+1 个节点和倒数第 k 个节点断开，并把后半部分拼接到链表的头部。

        T: O(N)
        S: O(1)
        """

        if not head or not head.next:
            return head

        # 求链表长度
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        # 对长度取模
        k %= n
        if k == 0:
            return head

        # 让 fast 先向后走 k 步
        fast, slow = head, head
        while k:
            fast = fast.next
            k -= 1
        # 此时 slow 和 fast 之间的距离是 k；fast 指向第 k+1 个节点
        # 当 fast.next 为空时，fast 指向链表最后一个节点，slow 指向倒数第 k + 1 个节点
        while fast.next:
            fast = fast.next
            slow = slow.next

        # newHead 是倒数第 k 个节点，即新链表的头
        newHead = slow.next
        # 让倒数第 k + 1 个节点 和 倒数第 k 个节点断开
        slow.next = None
        # 让最后一个节点指向原始链表的头
        fast.next = head

        return newHead

