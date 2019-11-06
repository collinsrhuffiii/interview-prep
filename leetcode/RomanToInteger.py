'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

class Solution:
    def romanToInt(self, s):
        symbolMap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        s_rev = s[::-1]
        ret_val = 0
        prev_val = 0
        for c in s_rev:
            cur_val = symbolMap[c]
            if cur_val < prev_val:
                ret_val -= cur_val
            else:
                ret_val += cur_val
            prev_val = cur_val
        return ret_val
        '''
        First Solution
        symbolMap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        retVal = 0
        n = len(s)
        i = 0
        while(i < n):
            if s[i] == 'I' and i<=n-2 and (s[i+1] == 'V' or s[i+1] == 'X'):
                    retVal += symbolMap[s[i+1]] - 1
                    i += 2
            elif s[i] == 'X' and i<=n-2 and (s[i+1] == 'L' or s[i+1] == 'C'):
                    retVal += symbolMap[s[i+1]] - 10
                    i += 2
            elif s[i] == 'C' and i<=n-2 and (s[i+1] == 'D' or s[i+1] == 'M'):
                    retVal += symbolMap[s[i+1]] - 100
                    i += 2
            else:
                retVal += symbolMap[s[i]]
                i += 1
        return retVal
        '''

sol = Solution()
roman = 'III'
print(f'Input: {roman}')
print(f'Output: {sol.romanToInt(roman)}')

roman = 'IV'
print(f'Input: {roman}')
print(f'Output: {sol.romanToInt(roman)}')

roman = 'IX'
print(f'Input: {roman}')
print(f'Output: {sol.romanToInt(roman)}')

roman = 'LVIII'
print(f'Input: {roman}')
print(f'Output: {sol.romanToInt(roman)}')

roman = 'MCMXCIV'
print(f'Input: {roman}')
print(f'Output: {sol.romanToInt(roman)}')
