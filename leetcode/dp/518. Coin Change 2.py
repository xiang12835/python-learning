# coding=utf-8


class Solution:
    def change(self, amount, coins):
        """

        dp[j]：凑成总金额j的货币组合数为dp[j]

        T: O(N*amount)
        S: O(amount)

        """

        dp = [0]*(amount + 1)
        dp[0] = 1
        # 遍历物品
        for i in range(len(coins)):
            # 遍历背包
            for j in range(coins[i], amount + 1):
                dp[j] += dp[j - coins[i]]
        return dp[amount]

if __name__ == "__main__":
    print(Solution().change(5, [1, 2, 5]))
