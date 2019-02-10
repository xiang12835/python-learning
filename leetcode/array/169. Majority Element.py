# coding = utf-8

"""
Given an array of size n, find the majority element. The majority element is the element that appears more than [ n/2 ] times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) / 2]


class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        idx, cnt = 0, 1

        for i in xrange(1, len(nums)):
            if nums[idx] == nums[i]:
                cnt += 1
            else:
                cnt -= 1
                if cnt == 0:
                    idx = i
                    cnt = 1

        return nums[idx]
