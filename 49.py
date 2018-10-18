'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        d = []
        for item in strs:
            temp = sorted(item)
            temp = "".join(temp)
            if temp not in d:
                d.append(temp)
                res[temp] = [item]
            else:
                res[temp].append(item)
        return list(res.values())