# coding=utf-8

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        思路：尽可能到达最远位置（贪心）。

        T : O(n)
        S : O(1)
        """
        n = len(nums)
        max_dis = 0  # 初始化当前能到达最远的位置
        for i in range(n):
            if i <= max_dis and i + nums[i] > max_dis:  # 如果当前位置能到达，并且当前位置+跳数>最远位置
                max_dis = i + nums[i]  # 更新最远能到达位置
        return max_dis >= i
