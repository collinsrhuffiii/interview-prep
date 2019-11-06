'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
'''

class Solution:
    def searchMatrix(self, matrix, target):
        def find(table, val):
            if (not table) or (not table[0]):
                return (-1,-1)
            rows = len(table)
            cols = len(table[0])

            # use recursive helper function
            return find_helper(table, val, 0, 0, rows, cols)


        def find_helper(table, val, row_start, col_start, row_end, col_end):
            # base case
            if(row_end-row_start<=1 and col_end-col_start<=1):
                if(table[row_start][col_start] == val):
                    return (row_start, col_start)
                else:
                    return (-1, -1)

            # recursive step

            row_mid = (row_start + row_end)//2
            col_mid = (col_start + col_end)//2
            mid_element = table[row_mid][col_mid]

            if(mid_element == val):
                return (row_mid, col_mid)

            if val > mid_element:
                # search upper right quadrant
                q1 = find_helper(table, val, row_start, col_mid, row_mid, col_end)
                # search lower left quadrant
                q2 = find_helper(table, val, row_mid, col_start, row_end, col_mid)
                # search lower right quadrant
                q3 = find_helper(table, val, row_mid, col_mid, row_end, col_end)
            else:  # val <= mid_element
                # search upper left quadrant
                q1 = find_helper(table, val, row_start, col_start, row_mid, col_mid)
                # search upper right quadrant
                q2 = find_helper(table, val, row_start, col_mid, row_mid, col_end)
                # search lower left quadrant
                q3 = find_helper(table, val, row_mid, col_start, row_end, col_mid)

            # check if any of the quadrants contained target val
            if q1 != (-1,-1):
                return q1
            if q2 != (-1,-1):
                return q2
            if q3 != (-1,-1):
                return q3

            # none of the quadrants contained target val
            return (-1,-1) 

        return (find(matrix, target) != (-1,-1))

sol = Solution()

print(sol.searchMatrix([],0))
