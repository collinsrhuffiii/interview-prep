'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is  able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution:
    def trap(self, height):
        if not height:
            return 0
        #DP solution
        n = len(height)

        max_left = [0 for _ in range(n)]
        max_right = [0 for _ in range(n)]
        max_left[0] = height[0]
        max_right[n-1] = height[n-1]
        for i in range(1,n):
            max_left[i] = max(height[i], max_left[i-1])
        for i in range(n-2, -1, -1):
            max_right[i] = max(height[i], max_right[i+1])

        water = 0
        for i in range(1,n-1):
            water += min(max_left[i], max_right[i]) - height[i]
        return water

        '''
        Stack Solution
        n = len(height)
        water = 0
        stack = []
        i = 0
        while i < n:
            if (not stack) or height[i] <= height[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                bot = stack.pop()
                if not stack:
                    max_water = 0
                else:
                    max_water = (min(height[stack[-1]], height[i]) - height[bot]) * (i - stack[-1] -1)
                water += max_water

        
        return water
        '''

sol = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(f'Input: {height}')
print(f'Output: {sol.trap(height)}')

height = [2,0,2]
print(f'Input: {height}')
print(f'Output: {sol.trap(height)}')

height = [2,1,0,1,2]
print(f'Input: {height}')
print(f'Output: {sol.trap(height)}')
