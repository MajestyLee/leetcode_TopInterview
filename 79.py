'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or
 vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''


class Solution:
    def exist(self, board, word):
        def helper(board, word, m, n, i, j):
            if len(word) == 0: return True
            if not (0 <= i <= m - 1) or not (0 <= j <= n - 1): return False
            if board[i][j] == word[0]:
                # Mark as 0 since we should not use the same value again.
                board[i][j] = '#'
                val = (
                        helper(board, word[1:], m, n, i - 1, j)
                        or helper(board, word[1:], m, n, i, j - 1)
                        or helper(board, word[1:], m, n, i, j + 1)
                        or helper(board, word[1:], m, n, i + 1, j)
                )
                # Fix the '0' mark
                board[i][j] = word[0]
                return val
            return False

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if helper(board, word, m, n, i, j): return True

        return False