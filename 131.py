'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s:
            return [[]]
        if len(s) == 1:
            return [[s]]
        result = []
        for i in range(len(s)):
            temp = s[:i + 1]
            if temp == s[i::-1]:
                for rem in self.partition(s[i + 1:]):
                    result.append([temp] + rem)
        return result