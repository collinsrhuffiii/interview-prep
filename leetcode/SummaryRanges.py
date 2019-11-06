'''
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Example 2:
Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
'''

class Solution:
    def summaryRanges(self, nums):
        if not nums:
            return []
        n = len(nums)
        if n == 1:
            return [str(nums[0])]

        summary = [nums[0]]
        ranges = []
        for i in range(1,n):
            if nums[i] != summary[-1] + 1:
                if len(summary) == 1:
                    ranges.append(str(summary[0]))
                else:
                    ranges.append(str(summary[0]) + '->' + str(summary[-1]))
                summary = []
            summary.append(nums[i])

        if len(summary) == 1:
            ranges.append(str(summary[0]))
        else:
            ranges.append(str(summary[0]) + '->' + str(summary[-1]))
        return ranges

sol = Solution()
nums = [0,1,2,4,5,7]
print(f'Input: {nums}')
print(f'Output: {sol.summaryRanges(nums)}')

nums = [0,2,3,4,6,8,9]
print(f'Input: {nums}')
print(f'Output: {sol.summaryRanges(nums)}')

nums = [0,2,3,4,6,8,9]
print(f'Input: {nums}')
print(f'Output: {sol.summaryRanges(nums)}')
