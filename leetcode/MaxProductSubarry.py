'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''

class Solution:
    def maxProduct(self, nums):
        n = len(nums)

        # max_product[i] = max product that can be achieved from among first i
        # nums, including nums[i]
        max_product = [0 for _ in range(n)]

        # min_product[i] = min product that can be achieved from among first i
        # nums, including nums[i]
        min_product = [0 for _ in range(n)]

        max_product[0] = nums[0]
        min_product[0] = nums[0]
        result = nums[0]

        for i in range(1,n):
            min_product[i] = min(nums[i],
                                 nums[i] * max_product[i-1],
                                 nums[i] * min_product[i-1])

            max_product[i] = max(nums[i],
                                 nums[i] * max_product[i-1],
                                 nums[i] * min_product[i-1])

            result = max(max_product[i], result)
        
        return result
                                 
            


sol = Solution()
nums = [2,3,-2,4]
print(f'Input: {nums}')
print(f'Output: {sol.maxProduct(nums)}')

nums = [-2,0,-1]
print(f'Input: {nums}')
print(f'Output: {sol.maxProduct(nums)}')
