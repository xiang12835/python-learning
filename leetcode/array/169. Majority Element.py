# coding=utf-8

"""
Given an array of size n, find the majority element. The majority element is the element that appears more than [ n/2 ] times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        排序
        """
        return sorted(nums)[len(nums) / 2]


class Solution1(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        字典记录出现次数，取次数最多对应的key即可

        """
        lookup = {}
        for num in nums:
            lookup[num] = lookup.get(num, 0) + 1
        max_occur = max(lookup.values())
        for key in lookup:
            if lookup[key] == max_occur:
                return key


class Solution2(object):
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


class Solution3(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int

这个问题有一个很出名的算法

Boyer-Moore众数(majority number) 问题

在数组中找到两个不相同的元素并删除它们，不断重复此过程，直到数组中元素都相同，那么剩下的元素就是主要元素。

这个算法的妙处在于不直接删除数组中的元素，而是利用一个计数变量.
        """
        count = 0
        tmp = None
        for n in nums:
            if count == 0:
                tmp = n

            if n == tmp:
                count += 1
            else:
                count -= 1

        return tmp