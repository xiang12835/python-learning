# coding=utf-8

"""
 Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return True if len(set(nums)) < len(nums) else False


class Solution1(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        集合
        """
        ss = set()
        for n in nums:
            if n in ss:
                return True
            ss.add(n)

        return False


class Solution2(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        排序
        """
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
