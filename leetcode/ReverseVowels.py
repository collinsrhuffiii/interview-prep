'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''
class Solution:
    def reverseVowels(self, s):
        vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
        vowels_in_s = []
        for c in s:
            if c in vowels:
                vowels_in_s.append(c)

        ret = ''
        for c in s:
            if c in vowels:
                ret += vowels_in_s.pop()
            else:
                ret += c
        return ret


