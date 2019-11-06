'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
'''

class Solution:
    def setZeroes(self, matrix):
        if not matrix:
            return

        # O(1) Space Solution

        rows = len(matrix)
        cols = len(matrix[0])
        col0 = 1
        for i in range(rows):
            if matrix[i][0] == 0:
                col0 = 0
            for j in range(1,cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(rows-1, -1, -1):
            for j in range(cols-1, 0, -1):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
            if col0 == 0:
                matrix[i][0] = 0

        '''
        O(m+n) Space Solution
        rows = len(matrix)
        cols = len(matrix[0])
        seen_rows = [0 for i in range(rows)]
        seen_cols = [0 for i in range(cols)]
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    seen_rows[i] = 1
                    seen_cols[j] = 1
        
        for i in range(rows):
            if seen_rows[i] == 1:
                for j in range(cols):
                    matrix[i][j] = 0
        for j in range(cols):
            if seen_cols[j] == 1:
                for i in range(rows):
                    matrix[i][j] = 0
        '''

sol = Solution()

matrix = [[0],[1]]
sol.setZeroes(matrix)
print(matrix)

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
sol.setZeroes(matrix)
print(matrix)
