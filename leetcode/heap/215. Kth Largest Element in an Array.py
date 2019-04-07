# coding=utf-8

"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
"""


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k-1]


class Solution1(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int

        现在打算只维护一个容量为k的小顶堆，最终堆顶的值就是结果
        https://love.ranshy.com/heapq-%E5%A0%86%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/

        """

        from heapq import heappush, heappop

        n = len(nums)
        heap = []
        for i in xrange(n):
            heappush(heap, nums[i])
            if len(heap) > k:
                heappop(heap)

        return heap[0]