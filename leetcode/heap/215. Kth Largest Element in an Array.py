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
        2. 排序后切片/索引

        T：O(nlogn)
        S：O(n)

        """

        # return sorted(nums)[-k]
        return sorted(nums, reverse=True)[k-1]


class Solution1(object):
    def findKthLargest(self, nums, k):
        """
        3. 使用堆，这里特指小根堆/最小堆

        T：O(nlogk)
        S：O(k)

        现在打算只维护一个容量为k的小顶堆，最终堆顶的值就是结果
        https://love.ranshy.com/heapq-%E5%A0%86%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84/

        """

        from heapq import heappush, heappop

        n = len(nums)
        heap = []
        for i in range(n):
            heappush(heap, nums[i])
            if len(heap) > k:
                heappop(heap)

        return heap[0]


class Solution2(object):
    """
    4. 使用类快排

    T：O(n)
    S：O(1)
    """
    def findKthLargest(self, nums, k):
        def partition(nums, left, right):
            pivot = nums[left]#初始化一个待比较数据
            i,j = left, right
            while(i < j):
                while(i<j and nums[j]>=pivot): #从后往前查找，直到找到一个比pivot更小的数
                    j-=1
                nums[i] = nums[j] #将更小的数放入左边
                while(i<j and nums[i]<=pivot): #从前往后找，直到找到一个比pivot更大的数
                    i+=1
                nums[j] = nums[i] #将更大的数放入右边
            #循环结束，i与j相等
            nums[i] = pivot #待比较数据放入最终位置
            return i #返回待比较数据最终位置

        #快速排序
        def quicksort(nums, left, right):
            if left < right:
                index = partition(nums, left, right)
                quicksort(nums, left, index-1)
                quicksort(nums, index+1, right)

        # 将快速排序改成快速选择，即我们希望寻找到一个位置，这个位置左边是k个比这个位置上的数更小的数，右边是n-k个比该位置上的数大的数，我将它命名为topk_split，找到这个位置后停止迭代，完成了一次划分。
        def topk_split(nums, k, left, right):
            #寻找到第k个数停止递归，使得nums数组中index左边是前k个小的数，index右边是后面n-k个大的数
            if (left<right):
                index = partition(nums, left, right)
                if index==k:
                    return
                elif index < k:
                    topk_split(nums, k, index+1, right)
                else:
                    topk_split(nums, k, left, index-1)

        #获得第k小的数
        def topk_small(nums, k):
            topk_split(nums, k, 0, len(nums)-1)
            return nums[k-1] #右边是开区间，需要-1


        #获得第k大的数
        def topk_large(nums, k):
            #parttion是按从小到大划分的，如果让index左边为前n-k个小的数，则index右边为前k个大的数
            topk_split(nums, len(nums)-k, 0, len(nums)-1) #把k换成len(nums)-k
            return nums[len(nums)-k]

        return topk_large(nums, k)
