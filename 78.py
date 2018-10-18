'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cur_dp = [[]]
        for i in range(0, len(nums)):
            pre_dp = [cur_dp[_] for _ in range(0, len(cur_dp))]
            for j in range(0, len(pre_dp)):
                if pre_dp[j]:
                    temp = [pre_dp[j][_] for _ in range(len(pre_dp[j]))]
                    temp.append(nums[i])
                    cur_dp.append(temp)
                else:
                    cur_dp.append([nums[i]])
        return cur_dp
