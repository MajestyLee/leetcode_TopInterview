'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low = 0
        high = len(nums)
        f = -1
        l = -1
        while (low < high):
            mid = (low+high)//2
            if mid==0:
                if nums[mid] == target:
                    f = mid
                    break
            if nums[mid] == target and nums[mid-1] < target:
                f = mid
                break
            elif nums[mid] > target or (nums[mid] == target and nums[mid+1 if mid+1<high else mid] >= target):
                high = mid
            else:
                low = mid + 1
        low = 0
        high = len(nums)
        while (low < high):
            mid = (low+high)//2
            if mid==high-1:
                if nums[mid] == target:
                    l = mid
                    break
            if nums[mid] == target and nums[mid+1 if mid+1<high else mid] > target:
                l = mid
                break
            elif nums[mid] < target or (nums[mid] == target and nums[mid-1 if mid > 0 else 0] <= target):
                low = mid + 1
            else:
                high = mid
        return [f,l]

a = Solution()
print(a.searchRange([2,2],2))
