'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

class Solution:
    def plusOne(self, digits):
        n = len(digits)
        rem = 1
        i = n-1
        while(i > -1 and rem > 0):
            sum_dig = 1 + digits[i]
            if sum_dig == 10:
                rem = 1
                digits[i] = 0
            else:
                rem = 0
                digits[i] = sum_dig
            i -= 1
        if rem == 1:
            digits.insert(0, 1)
        return digits

sol = Solution()
digs = [4,3,2,1]
print(f'Input: {digs}')
print(f'Output: {sol.plusOne(digs)}')

digs = [9,9,9,9]
print(f'Input: {digs}')
print(f'Output: {sol.plusOne(digs)}')
