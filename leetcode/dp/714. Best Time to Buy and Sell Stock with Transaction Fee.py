# coding=utf-8

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        """ dp 交易n次，含手续费

        T：O(n)
        S：O(1)

        1. subproblem

        2. dp arr

        dp[i][0] 表示第i天持有股票所省最多现金。

        dp[i][1] 表示第i天不持有股票所得最多现金

        3. dp equation

        如果第i天持有股票即dp[i][0]，那么可以由两个状态推出来

        第i-1天就持有股票，那么就保持现状，所得现金就是昨天持有股票的所得现金 即：dp[i - 1][0]
        第i天买入股票，所得现金就是昨天不持有股票的所得现金减去 今天的股票价格 即：dp[i - 1][1] - prices[i]
        所以：dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] - prices[i]);

        在来看看如果第i天不持有股票即dp[i][1]的情况，依然可以由两个状态推出来

        第i-1天就不持有股票，那么就保持现状，所得现金就是昨天不持有股票的所得现金 即：dp[i - 1][1]
        第i天卖出股票，所得现金就是按照今天股票价格卖出后所得现金，注意这里需要有手续费了即：dp[i - 1][0] + prices[i] - fee
        所以：dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee);

        """

        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = -prices[0] #持股票
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee) # 注意这里需要有手续费
        return max(dp[-1][0], dp[-1][1])


