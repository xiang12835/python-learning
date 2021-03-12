class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int

        T : O(n)
        S : O(1)
        """
        ans = 0
        for num in nums:
            if num == target:
                ans += 1

        return ans
