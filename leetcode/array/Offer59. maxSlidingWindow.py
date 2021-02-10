class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        T: O(n*k)
        """
        if not nums:
            return []

        n = len(nums)
        r = []
        for i in range(n-k+1):
            window = nums[i:i+k]
            r.append(max(window))
        return r
