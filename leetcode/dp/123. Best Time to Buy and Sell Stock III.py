# coding=utf-8

"""
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意: 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

输入: [3,3,5,0,0,3,1,4]
输出: 6
解释: 在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2:

输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: [7,6,4,3,1]
输出: 0
解释: 在这个情况下, 没有交易完成, 所以最大利润为 0。

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        第一维表示第i天，第二维表示交易了多少次，第三维表示是否持有股票

        """
        if not prices:
            return 0

        n = len(prices)
        profit = [[[0 for _ in xrange(2)] for _ in xrange(3)] for _ in xrange(n)]
        profit[0][0][0] = 0  # 第0天不持有股票，无交易，收益为0
        profit[0][0][1] = -prices[0]  # 第0天买入了一股，收益为-price[0]，注意，只有买了再卖了才算一笔交易
        profit[0][1][0] = float("-inf")  # 第0天买了又卖，收益为0
        profit[0][1][1] = float("-inf")  # 第0天买了又卖，再买
        profit[0][2][0] = float("-inf")  # 第0天无论交易多少次，收益都为0
        profit[0][2][1] = float("-inf")

        for i in range(1, n):
            profit[i][0][0] = profit[i-1][0][0]  # 不交易，不持有股票的情况下收益都是一样的
            profit[i][0][1] = max(profit[i-1][0][1], profit[i-1][0][0]-prices[i])

            profit[i][1][0] = max(profit[i-1][1][0], profit[i-1][0][1]+prices[i])
            profit[i][1][1] = max(profit[i-1][1][1], profit[i-1][1][0]-prices[i])

            profit[i][2][0] = max(profit[i-1][2][0], profit[i-1][1][1]+prices[i])  # 表示，要么不动，要么就是已经交易了一次，前一天还持有一只股，将它卖掉

        return max(profit[n-1][0][0], profit[n-1][1][0], profit[n-1][2][0])

