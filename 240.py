'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        """
        what I think is to find the medium thing in matrix, if target > medium, go down or          go right; else: go up or left
        """
        if len(matrix) <= 0:
            return False
        return self.dfsHelper(matrix, target, 0, len(matrix[0]) - 1)

    def dfsHelper(self, matrix, target, i, j):
        if j >= 0 and i < len(matrix):
            cur = matrix[i][j]
            if cur == target:
                return True
            elif cur > target:
                return self.dfsHelper(matrix, target, i, j - 1)
            else:
                return self.dfsHelper(matrix, target, i + 1, j)
        else:
            return False