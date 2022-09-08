# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxprofit = 0
        for i in range(0,len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]-prices[i]>maxprofit:
                    maxprofit = prices[j]-prices[i]
        return maxprofit
                    
