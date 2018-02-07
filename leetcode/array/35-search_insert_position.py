# coding=utf-8

# 对于排好序的数组进行插入的问题，为了减小算法的时间复杂度，很容易想到用二分查找的方法：


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) / 2 + left
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1

        return left
