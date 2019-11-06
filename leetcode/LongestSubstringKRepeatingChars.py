'''
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''

class Solution:
    def longestSubstring(self, s, k):
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


sol = Solution()
s = 'aaabb'
k = 3
print(f'Input: s = {s}, k = {k}')
print(f'Output: {sol.longestSubstring(s,k)}')

s = 'ababbc'
k = 2
print(f'Input: s = {s}, k = {k}')
print(f'Output: {sol.longestSubstring(s,k)}')

s = 'weitong'
k = 2
print(f'Input: s = {s}, k = {k}')
print(f'Output: {sol.longestSubstring(s,k)}')
