# coding=utf-8

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
1. 状态定义：
定义dp[i]表示第i天结束时的状态


dp[i][0]: 目前持有一只股票的最大收益
dp[i][1]: 目前不持有股票，且处于冷冻期的最大收益
dp[i][2]: 目前不持有股票，且不处于冷冻期的最大收益
问： 为什么状态定义中，持有股票的时候dp[i][0]不需要考虑冷冻期？
答： 因为今天持有股票，只可能是昨天买入的 或者 今天买入的，而买入都不考虑冷冻期，所以这里也不需要区分是否处于冷冻期了。

2. 转移方程
dp[i][0]（第i天结束时，持有一只股票）的转移来源：


a. 第i-1天持有股票，第i天什么都不做；
b. 第i-1天不持有股票且不处于冷冻期，则在第i天买入；

转移方程为：dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
dp[i][1]（第i天结束时，不持有股票，且处于冷冻期）的转移来源：


a. 第i-1天持有股票，在第i天卖掉；

转移方程为：dp[i][1] = dp[i-1][0] + prices[i]
dp[i][2]（第i天结束时，不持有股票，且不处于冷冻期）的转移来源：


a. 第i-1天不持有股票，且不处于冷冻期，第i天什么都不做；
b. 第i-1天不持有股票，且处于冷冻期，第i天什么都不做；

转移方程为：dp[i][2] = max(dp[i-1][2], dp[i-1][1])
3. 初始状态

dp[0] = [-prices[0], 0, 0]
        """
        if not prices:
            return 0

        dp = [[0] * 3 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1, len(prices)):
            # 根据转移方程编写代码
            dp[i][0] = max(dp[i-1][0], dp[i-1][2] - prices[i])
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1])
        return max(dp[-1])

