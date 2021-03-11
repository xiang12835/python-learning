# coding=utf-8

"""
 Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum+num)
            max_sum = max(cur_sum, max_sum)

        return max_sum


class Solution1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        最大子序和 = 当前元素自身最大 or 加上之前后最大
        dp[i] = max(nums[i], nums[i] + dp[i-1])
        """
        if len(nums) == 1:
            return nums[0]

        n = len(nums)

        dp = nums
        for i in xrange(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])

        return max(dp)
