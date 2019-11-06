'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

class Solution:
    def permute(self, nums):
        n = len(nums)
        permutations = []
        def swap(arr, i, j):
            new_arr = arr[:]
            new_arr[i], new_arr[j] = new_arr[j], new_arr[i]
            return new_arr
        def helper(index, permutation):
            if index == n-1:
                permutations.append(permutation)
                return
            for i in range(index, n):
                new_permutation = swap(permutation, index, i)
                helper(index + 1, new_permutation)

        helper(0, nums)
        return permutations

sol = Solution()
nums = [1,2,3]
print(f'Input: nums = {nums}')
print('Output:')
perm = sol.permute(nums)
for row in perm:
    print(row)
