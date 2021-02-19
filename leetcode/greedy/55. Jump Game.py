# coding=utf-8

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        T : O(n)
        S : O(1)
        """
        n = len(nums)
        dis = 0
        for i in range(n):
            if i <= dis:
                dis = max(dis, i + nums[i])
                if dis >= n - 1:
                    return True

        return False
