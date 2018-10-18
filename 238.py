'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
'''


class Solution(object):
    def handle(self, nums):
        result = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] == 0:
                break
        s = 1
        for num in nums:
            if num != 0:
                s *= num
        result[i] = s
        return result

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if nums.count(0) >= 2:
            return [0 for i in range(len(nums))]
        elif nums.count(0) == 1:
            return self.handle(nums)
        else:
            s = 1
            for num in nums:
                s *= num
            nums.count(0)
            return list(map(lambda x: s / x, nums))