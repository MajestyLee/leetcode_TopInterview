'''
You are given coins of different denominations and a total amount of money amount.
Write a function to compute the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''
import math

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [-1 for _ in range(0, amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            temp = []
            for coin in coins:
                if i - coin < 0:
                    continue
                else:
                    if dp[i - coin] == -1:
                        continue
                    else:
                        temp.append(dp[i - coin] + 1)
            if temp:
                dp[i] = min(temp)
        return dp[-1]

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # max_amount = amount + 1
        # dp = [max_amount for i in range(amount+1)]
        # dp[0] = 0
        # for i in range(amount+1):
        #     for j in coins:
        #         if j <= i:
        #             dp[i] = min(dp[i], dp[i-j] + 1)
        # if dp[amount] > amount:
        #     return -1
        # return dp[amount]
        def dfs(num, remain, count):
            coin = remain[0]
            if count + math.ceil(num / coin) >= self.result:
                return
            if num % coin == 0:
                self.result = count + num // coin
                return
            if len(remain) == 1:
                return
            for i in range(num // coin, -1, -1):
                dfs(num - coin * i, remain[1:], count + i)

        if amount == 0:
            return 0
        coins.sort(reverse=True)
        self.result = amount + 1
        dfs(amount, coins, 0)
        return self.result if self.result <= amount else -1
