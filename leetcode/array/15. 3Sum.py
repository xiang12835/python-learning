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

        T：O(N^2)，其中 N 是数组 nums 的长度。

        S：O(logN)。
        """
        nums.sort()
        n = len(nums)

        ans = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:  # 去重复
                continue
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]: # 去重复
                        l += 1
                    while l < r and nums[r] == nums[r+1]: # 去重复
                        r -= 1
        return ans

if __name__ == "__main__":
    s = Solution()
    print s.threeSum([-1,0,1,2,-1,-4])
