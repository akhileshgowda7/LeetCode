# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0


class Solution:
    def maxProfit(self, prices: [int]):
        val = []

        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[j]>prices[i]:
                    val.append(prices[j] - prices[i])

        print(val)
        print(max(val))
        return max(val)

Solution().maxProfit([7,1,5,3,6,4])
