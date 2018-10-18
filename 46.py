'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dp_cur = []
        dp_pre = [[nums[0]]]
        for i in range(2, len(nums) + 1):
            for item in dp_pre:
                for k in range(0,i):
                    item.insert(k, nums[i-1])
                    dp_cur.append([item[_] for _ in range(len(item))])
                    item.remove(nums[i-1])

            dp_pre = dp_cur
            dp_cur = []

        return dp_pre