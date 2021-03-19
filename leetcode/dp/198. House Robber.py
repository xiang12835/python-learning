# coding=utf-8

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

"""


class Solution1:
    def rob(self, nums: List[int]) -> int:
        """
        法一：

        DP + 升维

        1. subproblems
        2. dp array

        a[i][0,1]: 0 … i 能偷到 max value 0: 不偷 1: 偷

        3. dp equation

        a[i][0] = max(a[i-1][0], a[i-1][1])
        a[i][1] = a[i-1][0] + nums[i]

        T: O(N)
        S: O(N)
        """
        if not nums:
            return 0

        n = len(nums)

        # 初始化 dp
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = nums[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]

        return max(dp[n - 1][0], dp[n - 1][1])


class Solution2:
    def rob(self, nums: List[int]) -> int:
        """
        法二：

        DP + 降维

        使用两个一维的dp方程

        1. subproblems
        2. dp array

        a[i][0,1]: 0 … i 能偷到 max value 0: 不偷 1: 偷

        3. dp equation

        a[i][0] = max(a[i-1][0], a[i-1][1])
        a[i][1] = a[i-1][0] + nums[i]

        T: O(N)
        S: O(N)
        """

        if not nums:
            return 0

        n = len(nums)
        dp0 = [0] * n
        dp1 = [nums[0]] * n

        for i in range(1, n):
            dp0[i] = max(dp0[i - 1], dp1[i - 1])
            dp1[i] = dp0[i - 1] + nums[i]

        return max(dp0[n - 1], dp1[n - 1])


class Solution3:
    def rob(self, nums: List[int]) -> int:
        """
        法三：

        DP + 降维

        使用一个一维dp方程，优化dp方程

        dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        T: O(N)
        S: O(N)
        """

        if not nums:
            return 0

        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[n - 1]


class Solution4(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        法四：

        DP + 优化空间

        dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        T: O(N)
        S: O(1)
        """
        pre, cur = 0, 0
        for num in nums:
            pre, cur = cur, max(pre + num, cur)
        return cur


if __name__ == "__main__":
    s = Solution()
    print s.rob([1,2,3,1])
