'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

class Solution:
    def convert(self, s, numRows):
        n = len(s)
        if numRows == 1:
            return s
        step = 1
        row = 0
        output = ['' for i in range(numRows)]
        for c in s:
            if row == 0:
                step = 1
            if row == numRows-1:
                step = -1
            output[row] += c
            row += step
        return ''.join(output)

        '''
        First try
        while(i < n and i < numRows):
            if i == numRows-1:
                down = False
            else:
                down = True
            j = i
            output += s[j]
            while(j < n):
                if down:
                    j += 2*(numRows - i - 1)
                else:
                    j += 2*i
                if j < n:
                    output += s[j]
                if i != 0 and i != numRows-1:
                    down = not down
            i += 1
        return output
        '''


sol = Solution()

s = 'PAYPALISHIRING'
numRows = 3
print(f'Input: s = {s}, numRows = {numRows}')
print(f'Output: {sol.convert(s, numRows)}')

s = 'A'
numRows = 1
print(f'Input: s = {s}, numRows = {numRows}')
print(f'Output: {sol.convert(s, numRows)}')
