# coding=utf-8

"""

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false

"""


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        所以对于任何一个num来说，有三种可能：

        小于当前的最小值，那么更新当前最小值
        小于当前第二小值，更新当前第二小值
        如果以上两种都不是，那么是大于当前第二小值和最小值，于是这样就true

        所以是求四个增长也是类似的
        """
        first = second = float('inf')
        for v in nums:
            if v <= first:
                first = v
            elif v <= second:
                second = v
            else:
                return True
        return False
