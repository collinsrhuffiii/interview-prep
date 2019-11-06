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


import numpy as np
class Solution:
    '''
    DP
    P(i,j) = true if s[i:j+1] is a palindrome, false otherwise
    P(i,j) = true if P[i+1, j-1]==true, s[i] == s[j]
    '''
    def longestPalindrome(self, s):
        n = len(s)
        P = np.zeros((n,n))
        '''
        P = [[0 for i in range(n)] for i in range(n)]
        '''
        for i in range(n):
            P[i][i] = 1
        for i in range(n-1):
            P[i+1][i] = s[i] == s[i+1]

        max_len = (0,0,0)
        for i in range(n-2, -1, -1):
            for j in range(i):
                row = n-i + j
                col = j
                P[row][col] = P[row-1][col+1] == 1 and s[row] == s[col]
                if P[row][col] == 1:
                    max_len = max(max_len, (row - col, col, row), key=lambda
                            x:x[0])
        return s[max_len[1]: max_len[2]+1]




        

sol = Solution()
s = 'babad'
print(f'{s} : {sol.longestPalindrome(s)}')

s = 'cbbd'
print(f'{s} : {sol.longestPalindrome(s)}')

s = 'bb'
print(f'{s} : {sol.longestPalindrome(s)}')

s = 'abb'
print(f'{s} : {sol.longestPalindrome(s)}')

s = 'abba'
print(f'{s} : {sol.longestPalindrome(s)}')
