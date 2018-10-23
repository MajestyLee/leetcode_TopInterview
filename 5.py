'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb" 
'''
#brute force
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        n = len(s)
        index = [0,1]
        maxx = 1
        for i in range(1,n-1):
            j = i-1
            k = i+1
            cur_max = 1
            while j >= 0 and k < n:
                if s[j]==s[k]:
                    cur_max += 2
                    j -= 1
                    k += 1
                else:
                    break
            if cur_max > maxx:
                index[0] = j+1
                index[1] = k
                maxx = cur_max
        for i in range(0,n-1):
            cur_max = 0
            j = i
            k = i+1
            while j >= 0 and k < n:
                if s[j]==s[k]:
                    cur_max += 2
                    j -= 1
                    k += 1
                else:
                    break
            if cur_max > maxx:
                index[0] = j+1
                index[1] = k
                maxx = cur_max
        return s[index[0]:index[1]]