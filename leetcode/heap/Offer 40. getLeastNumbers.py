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

        大根堆 -- 最小k个元素
        求前k个最小用最大堆，求前k个最大用最小堆。

        步骤如下：
        1: 取数组前k个元素初始化堆，从最后一个非叶子节点开始到根节点来构建大根堆
        2: 当某个元素大于堆顶元素时，直接抛弃
        3: 当某个元素小于堆顶元素时，替换栈顶元素，再从堆顶重新构建大根堆


        k+1 个数开始遍历，如果当前遍历到的数比大根堆的堆顶的数要小，就把堆顶的数弹出，再插入当前遍历到的数。最后将大根堆里的数存入数组返回即可。在下面的代码中，由于 C++ 语言中的堆（即优先队列）为大根堆，我们可以这么做。而 Python 语言中的对为小根堆，因此我们要对数组中所有的数取其相反数，才能使用小根堆维护前 k 小值


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
