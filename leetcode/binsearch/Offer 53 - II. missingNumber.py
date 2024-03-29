# coding=utf-8

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == m:
                l = m + 1
            else:
                r = m - 1
        return l


class Solution1(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return sum(range(len(nums) + 1)) - sum(nums)
