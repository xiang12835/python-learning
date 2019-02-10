# coding=utf-8

"""

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1

Note:

Your algorithm should run in O(n) time and uses constant extra space.


"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1

        ss = set(nums)
        for i in range(1, len(nums)+2):  # 至少有两个整数
            if i not in ss:
                return i


if __name__ == '__main__':
    s = Solution()
    l = [1]

    print s.firstMissingPositive(l)
