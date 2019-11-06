'''

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
'''

class Solution:
    def missingNumber(self, nums):
        n = len(nums)+1
        return n*(n-1)/2 - sum(nums)
        '''
        num_set = set()
        n = len(nums) + 1
        for i in range(n + 1):
            num_set.add(i)
        for num in nums:
            num_set.remove(num)
        return num_set.pop()
        '''
