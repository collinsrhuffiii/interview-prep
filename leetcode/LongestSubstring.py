'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution:
    def lengthOfLongestSubstring(self, s):
        n = len(s)
        seen_chars = {}
        max_length = 0
        i = 0
        for j in range(n):
            if s[j] in seen_chars:
                i = max(seen_chars[s[j]], i)
            seen_chars[s[j]] = j+1
            max_length = max(max_length, j-i+1)
        return max_length

        '''
        #First try
        if not s:
            return 0
        n = len(s)
        max_length = 0
        cur_length = 0
        seen_chars = {}
        last_index = 0
        i = 0
        while(i < n):
            if s[i] not in seen_chars:
                seen_chars[s[i]] = i
                cur_length += 1
            else:
                max_length = max(cur_length, max_length)
                last_index = max(seen_chars[s[i]], last_index)
                cur_length = i - last_index
                seen_chars[s[i]] = i
            i += 1
        max_length = max(cur_length, max_length)
        return max_length
        '''

sol = Solution()

input_string = 'abcabcbb'
print(input_string, ' : ' , sol.lengthOfLongestSubstring(input_string))
input_string = 'bbbbb'
print(input_string, ' : ' , sol.lengthOfLongestSubstring(input_string))
input_string = 'pwwkew'
print(input_string, ' : ' , sol.lengthOfLongestSubstring(input_string))
input_string = ''
print(input_string, ' : ' , sol.lengthOfLongestSubstring(input_string))
input_string = 'c'
print(input_string, ' : ' , sol.lengthOfLongestSubstring(input_string))
input_string = 'dvdf'
print(input_string, ' : ' , sol.lengthOfLongestSubstring(input_string))
input_string = 'ckilbkd'
input_string = 'abba'
print(input_string, ' : ' , sol.lengthOfLongestSubstring(input_string))
