# coding=utf-8


"""

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        典型DP

        递推关系式：

        对于以num[i]结束的longest increasing subsequence的长度

        dp[i] = dp[j] + 1 if num[i] > num[j] else dp[i], which 0 <= j < i

        loop一圈，求出最长的

        1. subproblem

        2. dp array

        dp[i] 的值代表 nums 前 i 个数字的最长子序列长度

        3. dp equation

        当 nums[i]>nums[j] 时： nums[i] 可以接在 nums[j] 之后（此题要求严格递增），此情况下最长上升子序列长度为 dp[j] + 1；

        T : O(n**2)
        S : O(n)

        """
        if not nums or len(nums) == 0:
            return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
        return max(dp)




class Solution1(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import bisect

        if not nums or len(nums) == 0:
            return 0

        lis = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] > lis[-1]:
                lis.append(nums[i])
            else:
                # 要用bisect_left，因为如果插入到右边就相当于多append了一个，而不再是replace了
                lis[bisect.bisect_left(lis, nums[i])] = nums[i]

        return len(lis)
