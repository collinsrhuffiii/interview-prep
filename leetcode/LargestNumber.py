'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
'''


from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        def compare(x, y):
            if x + y > y + x:
                return 1
            elif x + y < y + x:
                return -1
            else:
                return 0

        num_strs = [str(num) for num in nums]
        num_strs.sort(key=cmp_to_key(compare), reverse=True)
        return str(int(''.join(num_str for num_str in num_strs)))


sol = Solution()
nums = [10,2]
print(f'Input: {nums}')
print(f'Output: {sol.largestNumber(nums)}')
nums = [3,30,34,5,9]
print(f'Input: {nums}')
print(f'Output: {sol.largestNumber(nums)}')
