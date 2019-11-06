'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''

class Solution:
    def firstUniqChar(self, s):
        num_chars = len(s)
        no_repeat = [True for i in range(num_chars)]
        char_dict = {}
        for i,c in enumerate(s):
            if c in char_dict:
                no_repeat[char_dict[c]] = False
                no_repeat[i] = False
                char_dict[c] = i
            else:
                char_dict[c] = i

        for i,val in enumerate(no_repeat):
            if val == True:
                return i
        return -1

