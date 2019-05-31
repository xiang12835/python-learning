# coding=utf-8

"""

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        ans = None
        diff = float('inf')

        nums.sort()

        for i in xrange(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = n - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]

                if tmp > target:
                    r -= 1
                    if abs(tmp - target) < diff:
                        diff = abs(tmp - target)
                        ans = tmp

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif tmp < target:
                    l += 1
                    if abs(tmp - target) < diff:
                        diff = abs(tmp - target)
                        ans = tmp

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                else:

                    return target

        return ans
