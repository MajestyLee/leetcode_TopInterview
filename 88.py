'''
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if nums1 == None:
            return nums2[:n] if nums2 != None else None
        if nums2 == None:
            return nums1 if nums1 != None else None
        for i in range(n):
            flag = False
            for j in range(0, m + n):
                if nums2[i] < nums1[j]:
                    nums1.pop()
                    nums1.insert(j, nums2[i])
                    flag = True
                    break
            if flag == False:
                for j in range(i, n):
                    nums1.pop()
                for j in range(i, n):
                    nums1.append(nums2[j])
                break
