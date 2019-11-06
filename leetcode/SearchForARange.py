'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''

class Solution:
    def searchRange(self, nums, target):
        def search(target):
            n = len(nums)
            lo = 0
            hi = n
            while lo < hi:
                mid = (lo + hi)//2
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        if not target in nums[lo:lo+1]:
            return [-1,-1]
        hi = search(target+1) - 1
        return [lo,hi]

        '''
        hi = n - 1
        lo = 0
        if target > nums[hi] or target < nums[lo]:
            return [-1, -1]
        while(hi > lo):
            mid = (hi + lo)//2
            if nums[mid] == target:
                hi = mid
                lo = mid
            if nums[mid] > target:
                hi = mid - 1
            if nums[mid] < target:
                lo = mid + 1
        if nums[lo] != target:
            return [-1, -1]

        while lo > -1 and nums[lo] == target:
            lo -= 1
        lo += 1
        while hi < n and nums[hi] == target:
            hi += 1
        hi -= 1
        return [lo, hi]
        '''

sol = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(f'Input: nums = {nums}, target = {target}')
print(f'Output: {sol.searchRange(nums, target)}')


nums = [5,7,7,8,8,10]
target = 6
print(f'Input: nums = {nums}, target = {target}')
print(f'Output: {sol.searchRange(nums, target)}')
