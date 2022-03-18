# coding=utf-8

"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""



# 快速排序
def quick_sort(lists, left, right):
    """
    通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
    然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

    :param lists:
    :param left:
    :param right:
    :return:
    """
    if left >= right:
        return lists
    pivot = lists[left]
    low = left
    high = right
    while left != right:
        while left < right and lists[right] >= pivot:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= pivot:
            left += 1
        lists[right] = lists[left]
    lists[right] = pivot
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)
    return lists


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution1(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        second = self.findMid(head)  # 找到链表后半段的head
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)

    def merge(self, l, r):  # O(NlgN)
        if not l or not r:
            return l or r
        dummy = head = ListNode(None)
        head.next = l
        while l and r:
            if l.val < r.val:
                head.next = l
                l = l.next
            else:
                head.next = r
                r = r.next
            head = head.next
        head.next = l or r  # l and r at least one is None
        return dummy.next

    def findMid(self, head):
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        return second


class Solution2(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        4->2->1->3
        """
        if not head or not head.next:
            return head
        l, m, r = ListNode(None), ListNode(None), ListNode(None)
        ll, mm, rr = l, m, r

        pivot = head.val
        while head:
            if head.val < pivot:
                ll.next = head
                ll = ll.next
            elif head.val == pivot:
                mm.next = head
                mm = mm.next
            else:
                rr.next = head
                rr = rr.next
            head = head.next

        ll.next, rr.next = None, None
        l.next = self.sortList(l.next)
        r.next = self.sortList(r.next)
        ll = l
        while ll.next:
            ll = ll.next
        ll.next = m.next
        mm.next = r.next
        return l.next

