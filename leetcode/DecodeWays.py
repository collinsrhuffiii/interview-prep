'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''

class Solution:
    def numDecodings(self, s):
        num_decodings = {}
        def helper(s):
            if s in num_decodings:
                return num_decodings[s]
            if not s:
                return 1
            if s[0] == '0':
                return 0
            num_one_digit = 0
            if s[0] != 0:
                num_one_digit = helper(s[1:])
            num_two_digit = 0
            if len(s) > 1:
                if int(s[:2]) <= 26 and int(s[:2]) > 0:
                    num_two_digit = helper(s[2:])
            num_decodings[s] = num_one_digit + num_two_digit
            return num_decodings[s]
        return helper(s)

sol = Solution()
s = '12'
print(f'Input: s = {s}')
print(f'Output: {sol.numDecodings(s)}')

s = '226'
print(f'Input: s = {s}')
print(f'Output: {sol.numDecodings(s)}')
