class Solution:
    def maxProfit(self,prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        max_profit = 0
        len_prices = len(prices)
        while i < len_prices:
            j = i + 1
            profit = 0
            while (j < len_prices) and (prices[j] > prices[i]):
                profit = max(profit, prices[j]-prices[i])
                j += 1
            max_profit = max(max_profit, profit)
            i = j

        return max_profit