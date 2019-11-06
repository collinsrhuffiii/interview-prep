'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''

class Solution:
    def titleToNumber(self, s):
        if len(s) == 1:
            return (ord(s) - 65) + 1

        exp = 0
        result = 0
        for char in s[::-1]:
            result += (ord(char) - 64) * (26**exp)
            exp += 1

        return result

sol = Solution()
s = 'A'
print(f'Input: {s}')
print(f'Output: {sol.titleToNumber(s)}')

s = 'AB'
print(f'Input: {s}')
print(f'Output: {sol.titleToNumber(s)}')

s = 'ZY'
print(f'Input: {s}')
print(f'Output: {sol.titleToNumber(s)}')

s = 'ZZ'
print(f'Input: {s}')
print(f'Output: {sol.titleToNumber(s)}')
