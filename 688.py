'''
On an NxN chessboard, a knight starts at the r-th row and c-th column and attempts to make exactly K moves.
The rows and columns are 0 indexed, so the top-left square is (0, 0), and the bottom-right square is (N-1, N-1).

A chess knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction,
 then one square in an orthogonal direction.
Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go
 off the chessboard) and moves there.
The knight continues moving until it has made exactly K moves or has moved off the chessboard. Return the probability
 that the knight remains on the board after it has stopped moving.
Example:
Input: 3, 2, 0, 0
Output: 0.0625
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
Note:
N will be between 1 and 25.
K will be between 0 and 100.
The knight always initially starts on the board.
'''
class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        #pr数组 剪枝（很巧妙，不是很懂）
        pr = [[[0] * K for j in range(N)] for i in range(N)]
        def probab(N, K, r, c):
            if K == 0:
                return 1
            elif pr[r][c][K - 1] > 0:
                return pr[r][c][K - 1]
            p = 0
            for move in [[1, 2], [2, 1], [-1, 2], [-2, 1], [-1, -2], [-2, -1], [1, -2], [2, -1]]:
                rr, cc = r + move[0], c + move[1]
                if -1 < rr < N and -1 < cc < N:
                    p += 0.125 * probab(N, K - 1, rr, cc)
            pr[r][c][K - 1], pr[c][r][K - 1] = p, p
            pr[r][N - 1 - c][K - 1], pr[c][N - 1 - r][K - 1] = p, p
            pr[N - 1 - r][c][K - 1], pr[N - 1 - c][r][K - 1] = p, p
            pr[N - r - 1][N - c - 1][K - 1], pr[N - c - 1][N - r - 1][K - 1] = p, p
            return p
        p = probab(N, K, r, c)
        return p

    #dp
    def knightProbability2(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dp = [[0 for _ in range(N)] for _ in range(N)]
        dp[r][c] = 1
        dic = (-2, 1), (-1, 2), (1, 2), (2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)
        for _ in range(K):
            next_dp = [[0 for _ in range(N)] for _ in range(N)]
            for r in range(N):
                for c in range(N):
                    if dp[r][c]:
                        for i, j in dic:
                            rr = r + i
                            cc = c + j
                            if 0 <= rr < N and 0 <= cc < N:
                                next_dp[rr][cc] += dp[r][c] / 8.0
            dp = next_dp
        return sum(map(sum, dp))