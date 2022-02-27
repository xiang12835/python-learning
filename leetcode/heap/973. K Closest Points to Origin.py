# coding=utf-8
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        T：O(nlogn)，其中 n 是数组 points 的长度。算法的时间复杂度即排序的时间复杂度。
        S：O(logn)，排序所需额外的空间复杂度为 O(logn)。
        '''
        return sorted(points, key=lambda x: (x[0] ** 2 + x[1] ** 2))[:k]


class Solution1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        T: O(nlogk)
        S: O(k)

        """

        import heapq

        q = [(-x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:k])]
        heapq.heapify(q)

        n = len(points)
        for i in range(k, n):
            x, y = points[i]
            dist = -x ** 2 - y ** 2
            heapq.heappushpop(q, (dist, i))

        ans = [points[identity] for (_, identity) in q]
        return ans

