'''
BEST TIME TO BUY AND SELL STOCKS 3
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
'''

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices == None or len(prices)==0:
            return 0
        profit = [0 for i in range(len(prices))]
        minus = prices[0]
        profit[0] = 0
        for i in range(1, len(prices)):
            if (prices[i]< minus):
                minus = prices[i]
            if (profit[i-1] < prices[i]-minus):
                profit[i] = prices[i]-minus
            else:
                profit[i] = profit[i-1]
        maxi = prices[-1]
        profits = profit[-1]
        for j in range(len(prices)-2,-1,-1):
            if maxi < prices[j]:
                maxi = prices[j]
            if profits < profit[j] + maxi - prices[j]:
                profits = profit[j] + maxi - prices[j]
        return profits