'''
1004. Max Consecutive Ones III
Medium

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

Example 2:

Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
Output: 10
Explanation: 
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

 

Note:

    1 <= A.length <= 20000
    0 <= K <= A.length
    A[i] is 0 or 1 
'''
from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        starting_points = []
        l = 0
        r = 0
        while l < len(A):
            if A[l] == 1:
                r = l
                while r < len(A) and A[r] == 1:
                    r += 1
                starting_points.append((l, r-1))
                l = r
            else:
                l += 1

        max_ones = 0
        for starting_point in starting_points:
            print(starting_point)
            l_reachable = [0]

            l_start = starting_point[0]
            l = l_start
            flips = 0
            while l >= 0 and flips <= K:
                while l >= 0 and A[l] == 1:
                    l -= 1
                l_reachable.append(l_start - max(l + 1, 0))
                flips += 1
                l -= 1
            len_l_reachable = len(l_reachable)
            l_reachable += [l_reachable[-1] for _ in range(max(0, (K + 1) - len_l_reachable))]


            r_reachable = [0]

            r_start = starting_point[1]
            r = r_start
            flips = 0
            while r < len(A) and flips <= K:
                while r < len(A) and A[r] == 1:
                    r += 1
                r_reachable.append(min(r - 1, len(A) - 1) - r_start)
                flips += 1
                r += 1
            len_r_reachable = len(r_reachable)
            r_reachable += [r_reachable[-1] for _ in range(max(0, (K + 1) - len_r_reachable))]

            print(l_reachable)
            print(r_reachable)

            for l_val, r_val in list(zip(l_reachable, r_reachable[::-1])):
                max_ones = max(max_ones, (r_start - l_start) + (l_val + r_val))

        return max_ones



sol = Solution()
a = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(a, k)
expected_output = 6
output = sol.longestOnes(a, k)
print(output, expected_output == output)
print()

a = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3
print(a, k)
expected_output = 10
output = sol.longestOnes(a, k)
print(output, expected_output == output)
