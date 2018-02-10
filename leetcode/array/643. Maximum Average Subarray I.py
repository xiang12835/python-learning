"""
 Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75

Note:

    1 <= k <= n <= 30,000.
    Elements of the given array will be in the range [-10,000, 10,000].

"""


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if len(nums) <= k:
            return sum(nums) / float(len(nums))

        max_sum = nums[0]
        for i in xrange(len(nums)):
            if i + k <= len(nums):
                cur_sum = sum(nums[i:i + k])
                max_sum = max(max_sum, cur_sum)
        return max_sum / float(k)


if __name__ == "__main__":
    s = Solution()
    print s.findMaxAverage([1,12,-5,-6,50,3], 4)
    print s.findMaxAverage([5], 1)
    print s.findMaxAverage([0,1,1,3,3], 4)
