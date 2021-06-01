# coding=utf-8

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curSum = maxSum = 0
        for i in range(1, len(prices)):
            curSum = max(0, curSum + prices[i] - prices[i - 1])
            maxSum = max(curSum, maxSum)
        return maxSum


class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        res = 0
        n = len(prices)
        profit = [[0 for _ in xrange(3)] for _ in xrange(n)]

        profit[0][0] = 0  # 没有买入股票时
        profit[0][1] = -prices[0]  # 之前有一股，还没有卖
        profit[0][2] = 0  # 之前有一股，现在卖

        for i in range(1, n):
            profit[i][0] = profit[i-1][0]
            profit[i][1] = max(profit[i-1][1], profit[i-1][0] - prices[i])
            profit[i][2] = profit[i-1][1] + prices[i]
            res = max(profit[i][0], profit[i][1], profit[i][2])

        return res

class Solution2:
    def maxProfit(self, prices):
        """
        T: O(n^2)
        S: O(1)
        """
        n = len(prices)
        max_profit = 0

        for i in range(n):
            for j in range(i+1, n):  # i+1 易错
                max_profit = max(max_profit, prices[j]-prices[i])

        return max_profit

class Solution3:
    def maxProfit(self, prices):
        """
        min_price : 历史最低点
        max_profit : 最大利润

        T: O(n)
        S: O(1)
        """
        min_price = max(prices)
        max_profit = 0
        for p in prices:
            min_price = min(p, min_price)
            max_profit = max(p - min_price, max_profit)

        return max_profit


