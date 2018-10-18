'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''
import math
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        seen = set()
        depth = 0

        queue = []
        queue.append(n)

        while queue:
            size = len(queue)
            depth += 1
            for i in range(size):
                node = queue.pop(0)
                if node in seen:
                    continue
                seen.add(node)
                for j in range(1, int(math.sqrt(node)) + 1):
                    les = node - j * j
                    if les == 0:
                        return depth
                    queue.append(les)
        return 0