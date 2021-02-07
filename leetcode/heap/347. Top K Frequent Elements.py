

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
        """
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1


        nums = list(set(nums))

        nums = sorted(nums, key=lambda num:d[num], reverse=True)
        return nums[:k]


if __name__ == "__main__":
    s = Solution()
    print s.topKFrequent([1,1,1,2,2,3], 2)
