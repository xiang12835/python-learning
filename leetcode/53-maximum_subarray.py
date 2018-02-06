class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(num, cur_sum+num)
            max_sum = max(cur_sum, max_sum)

        return max_sum
