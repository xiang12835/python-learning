# coding=utf-8

"""

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        暴力求解
        """
        if len(nums) == 1:
            return nums[0]

        r = nums[0]
        n = len(nums)
        for i in xrange(n):
            for j in xrange(i + 1, n + 1):

                tmp = nums[i:j]

                product = 1
                for v in tmp:
                    product = product * v
                r = max(r, product)

        return r


class Solution1(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        动态规划

        dp[i] = max(dp[i-1] * a[i],a[i])

        """
        n = len(nums)
        maxdp = [nums[0]] * n
        mindp = [nums[0]] * n

        for i in xrange(1, n):
            maxdp[i] = max(nums[i], maxdp[i - 1] * nums[i], mindp[i - 1] * nums[i])
            mindp[i] = min(nums[i], maxdp[i - 1] * nums[i], mindp[i - 1] * nums[i])

        return max(maxdp)


