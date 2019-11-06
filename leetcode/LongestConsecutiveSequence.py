'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        num_set = set(nums)
        max_seq = 1
        for num in num_set:
            cur_seq = 1
            if num-1 not in num_set:
                i = num+1
                while(i in num_set):
                    i += 1
                    cur_seq += 1
            max_seq = max(max_seq, cur_seq)
        return max_seq

sol = Solution()

nums = [100, 4, 200, 1, 3, 2]
print(f'Input: {nums}')
print(f'Output: {sol.longestConsecutive(nums)}')

nums = [1,2,0,1]
print(f'Input: {nums}')
print(f'Output: {sol.longestConsecutive(nums)}')

nums = [1,0,-1]
print(f'Input: {nums}')
print(f'Output: {sol.longestConsecutive(nums)}')

nums = [-1,1,2,0]
print(f'Input: {nums}')
print(f'Output: {sol.longestConsecutive(nums)}')
