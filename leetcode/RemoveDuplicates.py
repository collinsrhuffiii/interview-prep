'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
'''

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        n = len(nums)
        count = 1
        cur = nums[0]
        for i in range(n):
            if nums[i] != cur:
                count += 1
                nums[count-1] = nums[i]
                cur = nums[i]
        return count

            


        

sol = Solution()

nums = [1,1,2]
print(f'Input: {nums}')
print(f'Output: {sol.removeDuplicates(nums)}')
print(f'{nums}')
