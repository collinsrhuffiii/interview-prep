'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.
'''

class Solution:
    def kthSmallest(self, matrix, k):
        rows = len(matrix)
        cols = len(matrix[0])
        lo = matrix[0][0]
        hi = matrix[rows-1][cols-1] + 1
        while(lo < hi):
            mid = lo + (hi-lo)//2
            count = 0
            j = cols - 1
            for i in range(rows):
                while(j >= 0 and matrix[i][j] > mid):
                    j -= 1
                count += (j + 1)
            if count < k:
                lo = mid + 1
            else:
                hi = mid
        return lo




sol = Solution()
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8

print('Input: matrix = ')
for row in matrix:
    print(row)
print(f'k = {k}')
print(f'Output: {sol.kthSmallest(matrix, k)}')
