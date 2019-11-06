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
        len_s = len(s)
        wordSet = set(wordDict)
        prefix = [False for i in range(len_s+1)]
        prefix[0] = True
        for i in range(1,len_s+1):
            for j in range(i-1, -1, -1):
                if prefix[j]:
                    if s[j:i] in wordSet:
                        prefix[i] = True
                        break
        return prefix[len_s]


        '''
        Time Limit Exceeded
        dp = {}
        def helper(s):
            if s in dp:
                return dp[s]
            len_s = len(s)
            for word in wordDict:
                len_word = len(word)
                if len_s == len_word:
                    if s == word:
                        return True
                else:
                    ind = s.find(word)
                    if ind != -1:
                        if ind == 0:
                            if self.wordBreak(s[len_word:], wordDict):
                                dp[s] = True
                                return True
                        elif ind + len_word == len_s:
                            if self.wordBreak(s[:ind], wordDict):
                                dp[s] = True
                                return True
                        elif self.wordBreak(s[:ind], wordDict) and self.wordBreak(s[ind+len(word):], wordDict):
                            dp[s] = True
                            return True
            dp[s] = False
            return False
        return helper(s)
        '''

sol = Solution()
s = "leetcode"
wordDict = ["leet", "code"]
print(f'Input:, {s}, {wordDict}') 
print(f'Output: {sol.wordBreak(s, wordDict)}')

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(f'Input:, {s}, {wordDict}') 
print(f'Output: {sol.wordBreak(s, wordDict)}')

s = "applepenapple"
wordDict = ["apple", "pen"]
print(f'Input:, {s}, {wordDict}') 
print(f'Output: {sol.wordBreak(s, wordDict)}')
