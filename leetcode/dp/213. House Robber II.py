# coding=utf-8

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        环状排列意味着第一个房子和最后一个房子中只能选择一个偷窃，因此可以把此环状排列房间问题约化为两个单排排列房间子问题：

        1 在不偷窃第一个房子的情况下（即 nums[1:]），最大金额是 p1

        2 在不偷窃最后一个房子的情况下（即 nums[:n−1]），最大金额是 p2

        ​综合偷窃最大金额：为以上两种情况的较大值，即 max(p1,p2)

        198. 打家劫舍

        T: O(N)
        S: O(N)
        """

        n = len(nums)
        if n == 0:
            return 0

        if n <= 2:
            return max(nums)

        # 不抢第一个
        dp1 = [0] * n
        dp1[0] = 0  # 注意，此时 dp1[0] = 0
        dp1[1] = nums[1]
        for i in range(2, n):
            dp1[i] = max(dp1[i - 1], nums[i] + dp1[i - 2])

        # 不抢最后一个
        dp2 = [0] * n
        dp2[0] = nums[0]
        dp2[1] = max(nums[0], nums[1])
        for i in range(2, n - 1):  # 注意，此时 dp2[n-1] = 0
            dp2[i] = max(dp2[i - 1], nums[i] + dp2[i - 2])

        return max(dp1[n - 1], dp2[n - 2])
