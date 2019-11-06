'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
'''

class Solution:
    def sortColors(self, nums):
        count = [0,0,0]
        for num in nums:
            count[num] += 1

        cur = 0
        for i in range(len(nums)):
            while not count[cur]:
                cur += 1
            nums[i] = cur
            count[cur] -= 1


sol = Solution()
nums = [2,0,2,1,1,0]
print(f'Input: nums = {nums}')
sol.sortColors(nums)
print(f'Outpit: {nums}')
