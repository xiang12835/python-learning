# coding=utf-8

"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:

Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.

Example 2:

Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.

Example 3:

Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
"""


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))

        if len(nums) == 0:
            return 0

        if len(nums) < 3:
            return sorted(nums)[-1]

        return sorted(nums, reverse=True)[2]


class Solution1(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = float("-inf")  # 负无穷
        for num in nums:
            if num in [first, second, third]:
                continue
            if num > first:
                second, third = first, second
                first = num
            elif num > second:
                third = second
                second = num
            elif num > third:
                third = num
        return third if third != float("-inf") else first
