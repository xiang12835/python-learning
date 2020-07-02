# coding=utf-8

"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
"""


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int

        heapq.merge(*iterables) 将多个列表合并，并进行堆调整，返回的是合并后的列表的迭代器

        import heapq
        return list(heapq.merge(*matrix))[k-1]

        """
        tmp = []
        for row in matrix:
            for col in row:
                tmp.append(col)

        return sorted(tmp)[k - 1]
