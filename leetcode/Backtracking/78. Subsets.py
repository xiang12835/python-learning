# coding=utf-8

"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        self.helper(0, [], nums, res)
        return res

    def helper(self, i, tmp, nums, res):
        res.append(tmp)
        for j in range(i, len(nums)):
            self.helper(j + 1, tmp + [nums[j]], nums, res)


if __name__ == "__main__":
    print Solution().subsets([1,2,3])

