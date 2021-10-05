"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        r = []

        length = len(nums)

        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    r = [i, j]
                    break

        return r


class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, v in enumerate(nums):
            if target - v in d:
                return [d[target - v], i]
            else:
                d[v] = i
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))

    s1 = Solution1()
    print(s1.twoSum([3, 2, 4], 6))
