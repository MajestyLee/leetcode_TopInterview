'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
calculate the max/min number in the current position.
'''
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max, curr_min = 1, 1
        best = max(nums)
        for n in nums:
            choices = [curr_max * n, curr_min * n, n]
            curr_max, curr_min = max(choices), min(choices)
            # maximum/minimum with this number
            best = max(best, curr_max)
            # update best so far
        return best
