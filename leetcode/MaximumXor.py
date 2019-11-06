'''
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
'''

class Solution:
    def findMaximumXOR(self, nums):
        max_xor = 0
        mask = 0
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            prefix_set = set()
            for num in nums:
                prefix_set.add(num & mask)

            greedy = max_xor | (1 << i)

            for prefix in prefix_set:
                cur = prefix ^ greedy
                if cur in prefix_set:
                    max_xor = greedy
        return max_xor

        '''
        Time Limit Exceeded
        n = len(nums)
        if n <= 1:
            return 0
        max_xor = nums[0] ^ nums[0]
        for i in range(n):
            for j in range(i,n):
                max_xor = max(max_xor, nums[i]^nums[j])
        return max_xor
        '''

sol = Solution()
nums =  [3, 10, 5, 25, 2, 8]
print(f'Input: {nums}')
print(f'Output: {sol.findMaximumXOR(nums)}')
