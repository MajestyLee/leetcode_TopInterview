'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = list(str(n))
        loop = []
        strr = []
        while True:
            if n == 1:
                return True
            if n in loop and "1" not in strr:
                return True
            if n in loop and "1" in strr:
                return False
            loop.append(n)
            n = 0
            for m in s:
                n += int(m) * int(m)
                strr.append(m)
            s = list(str(n))
