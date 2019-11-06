'''
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?
'''

class Solution:
    def isPowerOfThree(self, n):
        if n == 1 or n == 3:
            return True
        def helper(n):
            if n == 3:
                return True
            if n < 3:
                return False
            return helper(n/3)
        return helper(n)

sol = Solution()
n = 9
print(f'Input: {n}')
print(f'Output: {sol.isPowerOfThree(n)}')

n = 27
print(f'Input: {n}')
print(f'Output: {sol.isPowerOfThree(n)}')

n = 8
print(f'Input: {n}')
print(f'Output: {sol.isPowerOfThree(n)}')
