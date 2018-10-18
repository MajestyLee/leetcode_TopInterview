'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #dp problem
        #init the dp
        dp = [True] + [False] * len(s)
        #for each dp position, go through the list of words, and check if you able to find          a True position before position i.
        #for each position before that we able to complete it, we will mark it as true.
        #then return dp[-1]
        for i in range(1, len(dp)):
            for word in wordDict:
                len_word = len(word)
                if i - len_word >= 0 and dp[i - len_word]==True and s[i-len_word:i]==word:
                    dp[i] = True
        #print(dp)
        return dp[-1]