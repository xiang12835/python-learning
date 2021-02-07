# coding=utf-8

"""
 Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:

    You may assume k is always valid, 1 <= k <= number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]

        法一：字典 + 排序
        T: O(nlogn)
        S: O(n)

        """
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        # for n in nums:
        #     d[n] = d.get(n, 0) + 1


        nums = list(set(nums))

        nums = sorted(nums, key=lambda num:d[num], reverse=True)
        return nums[:k]


class Solution1:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """

        法二：去构建一个大顶堆，然后去删除k次，取k个最大值

        T: O(nlogn)
        S: O(n)
        """

        d = collections.Counter(nums)
        hp, ans = [], []
        for i in d:
            heapq.heappush(hp, (-d[i], i))
        for _ in range(k):
            ans.append(heapq.heappop(hp)[1])  # 每删除一个都需要调整堆
        return ans


if __name__ == "__main__":
    s = Solution()
    print s.topKFrequent([1,1,1,2,2,3], 2)
