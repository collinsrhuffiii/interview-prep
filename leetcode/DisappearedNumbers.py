'''
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
'''

class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        num_set = set()
        for i in range(1,n+1):
            num_set.add(i)
        for num in nums:
            if num in num_set:
                num_set.remove(num)
        return list(num_set)

sol = Solution()
nums = [4,3,2,7,8,2,3,1]
print(f'Input: {nums}')
print(f'Output: {sol.findDisappearedNumbers(nums)}')
