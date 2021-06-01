# coding=utf-8

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        1. subproblem
        假设数组 cost 的长度为 n，则 n 个阶梯分别对应下标 0 到 n−1，楼层顶部对应下标 n，问题等价于计算达到下标 n 的最小花费

        2. dp array
        创建长度为 n+1 的数组 dp，其中 dp[i] 表示达到下标 i 的最小花费。

        由于可以选择下标 0 或 1 作为初始阶梯，因此有 dp[0]=dp[1]=0。

        3. dp equation
        dp[i]=min(dp[i−1]+cost[i−1],dp[i−2]+cost[i−2])

        述代码的时间复杂度和空间复杂度都是 O(n)。

        注意到当 i≥2 时，dp[i] 只和 dp[i−1] 与 dp[i−2] 有关，因此可以使用滚动数组的思想，将空间复杂度优化到 O(1)。
        """

        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[-1]