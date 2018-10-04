# coding=utf-8

"""

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


"""


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        以 <num, index> 的形式存进字典里，如果 num 再次出现了，计算相邻距离，小于等于 k 则 return true，否则更新字典中元素的位置
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d = {}

        for i, v in enumerate(nums):
            if v in d:
                if i - d[v] <= k:
                    return True

                d[v] = i
            else:
                d[v] = i

        return False


class Solution1:
    def containsNearbyDuplicate(self, nums, k):
        """

        结合使用滑动窗口和查找表，不断查找当前滑动窗口内有没有重复值。我们通过建立一个 record 查找表，表中存的是窗口中的数，另外我们要注意的是，当窗口的大小 > k 的时候，我们要移除 record 中最左边的元素（保证我们窗口中有 <= k 个数）。

        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        n = len(nums)

        if (n <= 1):
            return False

        recode = set()

        for i in range(n):
            if nums[i] in recode:
                return True
            recode.add(nums[i])
            if len(recode) > k:
                recode.remove(nums[i - k])

        return False
