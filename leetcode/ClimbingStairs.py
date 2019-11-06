'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

class Solution:
    def climbStairs(self, n):
        if n <= 3:
            return n
        num_ways = [0 for _ in range(n+1)]
        num_ways[0] = 0
        num_ways[1] = 1
        num_ways[2] = 2
        for i in range(3, n+1):
            num_ways[i] = num_ways[i-1] + num_ways[i-2]
        return num_ways[n]

sol = Solution()
n = 2
print(f'Input: n = {n}')
print(f'Output: {sol.climbStairs(n)}')

n = 3
print(f'Input: n = {n}')
print(f'Output: {sol.climbStairs(n)}')

n = 4
print(f'Input: n = {n}')
print(f'Output: {sol.climbStairs(n)}')
