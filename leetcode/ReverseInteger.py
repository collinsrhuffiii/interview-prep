'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers 
within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose 
of this problem, assume that your function returns 0 when the reversed 
integer overflows.
'''

class Solution:
    def reverse(self, x):
        #Second Attempt - Faster
        if x < 0:
            y = -1 * int(str(-x)[::-1])
        else:
            y = int(str(x)[::-1])
        if y > 2**31 -1 or y < -2**31:
            y = 0
        return y

        ''' 
        First try - Correct
        if x < 0:
            negative = True
        else:
            negative = False
        str_num = str(x)
        output = ''
        if negative:
            for i in range(len(str_num)-1, 0, -1):
                output += str_num[i]         
        else:
            for i in range(len(str_num)-1, -1, -1):
                output += str_num[i]         

        output = int(output)
        if negative: output = -output
        if output > 2**31 - 1 or output < -2**31:
            return 0
        else:
            return output
        '''

sol = Solution()

input_num = -123
print(f'Input: {input_num}')
print(f'Output: {sol.reverse(input_num)}')
            
