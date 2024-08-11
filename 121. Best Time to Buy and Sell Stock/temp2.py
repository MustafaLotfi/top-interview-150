import time

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        most_profit = 0
        for i in range(1, len(prices)):
            for j in range(len(prices)):
                if (i + j) < len(prices):
                    diff = prices[j+i] - prices[j]
                    if diff > most_profit:
                        most_profit = diff

        return most_profit

print(Solution().maxProfit([7,1,5,3,6,4]))