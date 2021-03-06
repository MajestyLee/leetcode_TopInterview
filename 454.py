'''
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''
#2 SUM extension
import collections


class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # ab = {}
        # for i in A:
        #     for j in B:
        #         if i+j not in ab:
        #             ab[i+j] = 1
        #         else:
        #             ab[i+j] += 1
        # cd = {}
        # for i in C:
        #     for j in D:
        #         if i+j not in cd:
        #             cd[i+j] = 1
        #         else:
        #             cd[i+j] += 1
        # result  = 0
        # for (key,value) in ab.items():
        #     for (key2,value2) in cd.items():
        #         if key + key2 == 0:
        #             result = result + value*value2
        # return result

        AB = collections.Counter(a + b for a in A for b in B)
        return sum(AB[-c - d] for c in C for d in D)