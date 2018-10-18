'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        re = []
        for digit in digits:
            re.append(d[digit])
        n = len(re)
        stack = []
        result = [""]
        for i in range(n):
            pre = result
            temp = list(re[i])
            result = []
            for j in range(0,len(temp)):
                for p in pre:
                    result.append(p+temp[j])
        if len(result) == 1:
            return []
        return result