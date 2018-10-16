'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        su = []
        l = list(s)
        for i in s:
            if i not in su:
                su.append(i)
        for item in su:
            if l.count(item)==1:
                return l.index(item)
        return -1