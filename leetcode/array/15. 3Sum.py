# coding=utf-8

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        排序算法；左右碰撞
        """
        n, ans = len(nums), []

        nums.sort()

        for i in xrange(n):
            if i > 0 and nums[i] == nums[i - 1]:  # 因为i=0这个元素会直接往下执行；去重复
                continue

            l, r = i + 1, n - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:  # 去重复
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:  # 去重复
                        r -= 1
                elif tmp > 0:
                    r -= 1
                else:
                    l += 1
        return ans
