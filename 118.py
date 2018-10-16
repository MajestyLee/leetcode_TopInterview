'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
'''
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[] for _ in range(0,numRows)]
        for i in range(numRows):
            result[i] = [1 for _ in range(i+1)]
            if i >= 2:
                for j in range(1,i):
                    result[i][j] = result[i-1][j-1]+result[i-1][j]
        return result