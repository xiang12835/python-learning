# coding=utf-8

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """
        法一：排序

        T：O(nlogn)，其中 n 是数组 arr 的长度。
        S：O(logn)
        """
        return sorted(arr)[:k]


class Solution1:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        """
        法二：大顶堆

        T：O(nlogk)，其中 n 是数组 arr 的长度，大根堆 k 个元素
        S：O(logk)
        """

        import heapq
        if k == 0:
            return []

        hp = [-x for x in arr[:k]]  # Python 语言中的对为小根堆，因此我们要对数组中所有的数取其相反数，才能使用小根堆维护前 k 小值
        heapq.heapify(hp)  # 堆化
        for i in range(k, len(arr)):
            if arr[i] < -hp[0]:  # 如果当前遍历到的数比大根堆的堆顶的数要小
                heapq.heappop(hp)  # 把堆顶的数弹出
                heapq.heappush(hp, -arr[i])  # 再插入当前遍历到的数
        ans = [-x for x in hp]
        return ans
