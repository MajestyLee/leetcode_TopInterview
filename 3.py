'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
'''

#slide window two poniter O(n) in the loop, update the start postion and end position. using the dictionary to store

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_seen = {}
        longest = 0
        start = 0

        for i, char in enumerate(s):
            if char in last_seen and start <= last_seen[char]:
                last_start = start
                start = last_seen[char] + 1
                last_seen[char] = i
            else:
                last_seen[char] = i
                longest = max(longest, i - start + 1)

        return longest