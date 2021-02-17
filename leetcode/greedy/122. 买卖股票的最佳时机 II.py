class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        greedy

        T: O(n)
        S: O(1)
        """
        size = len(prices)

        r = 0
        for i in range(1, size):
            if prices[i] > prices[i - 1]:
                r += prices[i] - prices[i - 1]

        return r
