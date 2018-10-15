'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
class Solution(object):
    def fill(self, s,ln,rn):
        if ln == 0:
            for i in range(rn):
                s += ')'
            return [s]
        if ln == rn:
            return self.fill(s+'(',ln-1,rn)
        if ln < rn:
            return self.fill(s+'(',ln-1,rn) + self.fill(s+')', ln,rn-1)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        return self.fill('',n,n)