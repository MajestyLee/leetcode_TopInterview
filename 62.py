'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
'''
#DP
import math


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for j in range(0,m)] for i in range(0,n)]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
        #dfs
    def dfsUniquePaths(self,m,n):
        if m==1 or n == 1:
            return 1
        else:
            return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
        #math
    def mathUniquePaths(self, m, n):
        return math.factorial(m+n-2)/math.factorial(m-1)/math.factorial(n-1)

