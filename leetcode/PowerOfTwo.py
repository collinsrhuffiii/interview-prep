'''
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Example 2:

Input: 16
Output: true
Example 3:

Input: 218
Output: false
'''

class Solution:
    def isPowerOfTwo(self, n):
        count = 0
        for i in range(64):
            mask = (1 << i)
            if mask & n:
                if count:
                    return False
                else:
                    count += 1
        return count == 1

