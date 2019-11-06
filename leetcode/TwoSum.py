'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

class Solution:
    def twoSum(self, nums, target):
        diffs = {}
        for i in range(len(nums)):
            cur_diff = target - nums[i]
            if cur_diff in diffs:
                return [diffs[cur_diff], i]
            else:
                diffs[nums[i]] = i

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
