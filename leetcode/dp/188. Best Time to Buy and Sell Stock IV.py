# coding=utf-8

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        """ dp

        T：O(n * k)
        S：O(n * k)
        """

        if len(prices) == 0:
            return 0
        dp = [[0] * (2*k+1) for _ in range(len(prices))] # 至多有K笔交易，那么j的范围就定义为 2 * k + 1 就可以了
        for j in range(1, 2*k, 2):  # dp[0][j]当j为奇数的时候都初始化为 -prices[0]
            dp[0][j] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(0, 2*k-1, 2):
                dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j] - prices[i])  # 奇数就是买入
                dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1] + prices[i]) # 偶数就是卖出
        return dp[-1][2*k]
