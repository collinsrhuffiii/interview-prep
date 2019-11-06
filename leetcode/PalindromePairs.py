'''
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
'''

class Solution:
    def palindromePairs(self, words):
        def checkPalindrome(s):
            high = len(s)-1
            low = 0
            while(high > low):
                if s[high] != s[low]:
                    return False
                high -= 1
                low += 1
            return True

        indices = []
        n_words = len(words)
        if not words or n_words < 2:
            return indices
        table = {}
        for i in range(n_words): 
            table[words[i]] = i
        
        for i in range(n_words):
            for j in range(len(words[i])+1):
                string1 = words[i][:j]
                string2 = words[i][j:]
                string1_rev = string1[::-1]
                string2_rev = string2[::-1]
                if checkPalindrome(string1):
                    if string2_rev in table and table[string2_rev] != i:
                        indices.append([table[string2_rev], i])
                if checkPalindrome(string2):
                    if string1_rev in table and table[string1_rev] != i and len(string2) != 0:
                        indices.append([i, table[string1_rev]])
        return indices

            
    '''
    Time Limit Exceeded
    def palindromePairs(self, words):
        def checkPalindrome(s):
            s_rev = s[::-1]
            for i in range(len(s)):
                if s[i] != s_rev[i]:
                    return False
            return True

        indices = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if checkPalindrome(words[i]+words[j]):
                        indices.append([i,j])
        return indices
    '''

sol = Solution()
words = ["bat", "tab", "cat"]
print(f'Input: {words}')
print(f'Output: {sol.palindromePairs(words)}')

words = ["abcd", "dcba", "lls", "s", "sssll"]
print(f'Input: {words}')
print(f'Output: {sol.palindromePairs(words)}')

words = ["a",""]
print(f'Input: {words}')
print(f'Output: {sol.palindromePairs(words)}')
