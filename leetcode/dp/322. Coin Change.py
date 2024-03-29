# coding=utf-8

"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
"""


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int

        dp定义: 目标金额amount = i时， 至少需要dp[i]个硬币
        T：O(N*amount) = O(N)
        S：O(amount)
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:  # 枚举硬币种数
            for x in range(coin, amount + 1):  # 从小到大枚举金额，确保x - coin >= 0.
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1  # 如果为inf说明状态不可达，返回-1即可。

if __name__ == "__main__":
    print Solution().coinChange([1, 2, 5], 11)
