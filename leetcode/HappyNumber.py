'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
'''

class Solution:
    def isHappy(self, n):
        if n == 1: return True
        seen = set()
        seen.add(n)
        def helper(n):
            digits = [int(d) for d in str(n)]
            digits = [d**2 for d in digits]
            sum_digits = sum(digits)
            if sum_digits in seen:
                return False
            seen.add(sum_digits)
            if sum_digits == 1:
                return True
            else:
                return helper(sum_digits)
        return helper(n)

sol = Solution()
n = 2
print(f'Input: {n}')
print(f'Output: {sol.isHappy(n)}')
