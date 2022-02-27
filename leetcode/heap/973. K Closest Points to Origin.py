# coding=utf-8
from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        T：O(nlogn)，其中 n 是数组 points 的长度。算法的时间复杂度即排序的时间复杂度。
        S：O(logn)，排序所需额外的空间复杂度为 O(logn)。
        '''
        return sorted(points, key=lambda x: (x[0] ** 2 + x[1] ** 2))[:k]


class Solution1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """ 大顶堆

        我们可以使用一个大根堆实时维护前 kk 个最小的距离平方。

        首先我们将前 k 个点的编号（为了方便最后直接得到答案）以及对应的距离平方放入大根堆中，随后从第 k+1 个点开始遍历：如果当前点的距离平方比堆顶的点的距离平方要小，就把堆顶的点弹出，再插入当前的点。当遍历完成后，所有在大根堆中的点就是前 k 个距离最小的点。

        不同的语言提供的堆的默认情况不一定相同。在 C++ 语言中，堆（即优先队列）为大根堆，但在 Python 语言中，堆为小根堆，因此我们需要在小根堆中存储（以及比较）距离平方的相反数。

        T: O(nlogk)
        S: O(k)

        https://leetcode-cn.com/problems/k-closest-points-to-origin/solution/zui-jie-jin-yuan-dian-de-k-ge-dian-by-leetcode-sol/

        """

        q = [(-x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:k])]
        heapq.heapify(q)

        n = len(points)
        for i in range(k, n):
            x, y = points[i]
            dist = -x ** 2 - y ** 2
            heapq.heappushpop(q, (dist, i))

        ans = [points[identity] for (_, identity) in q]
        return ans

