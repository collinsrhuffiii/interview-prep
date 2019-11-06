'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''
class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        subseq = [0 for i in range(n)]
        subseq[0] = 1
        overall_max_len = 1
        for i in range(1,n):
            max_len = 1
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    max_len = max(max_len, subseq[j]+1)
            subseq[i] = max_len
            overall_max_len = max(overall_max_len, max_len)
        return overall_max_len

sol = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(f'Input: {nums}')
print(f'Output: {sol.lengthOfLIS(nums)}')

nums = [1,3,6,7,9,4,10,5,6]
print(f'Input: {nums}')
print(f'Output: {sol.lengthOfLIS(nums)}')
