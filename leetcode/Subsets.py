'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

class Solution:
    def subsets(self, nums):
        result = []
        n = len(nums)
        def subset_rec(i, cur):
            print(cur)
            if i == n:
                result.append(cur)
                return
            subset_rec(i+1, cur+[nums[i]])
            subset_rec(i+1, cur)

        
        subset_rec(0, [])
        return result

sol = Solution()
nums = [1,2]
print(f'Input: {nums}')
print(f'Output: {sol.subsets(nums)}')
