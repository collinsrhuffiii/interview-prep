'''
542. 01 Matrix
Medium

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.


Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]


Note:

    The number of elements of the given matrix will not exceed 10,000.
    There are at least one 0 in the given matrix.
    The cells are adjacent in only four directions: up, down, left and right.

'''

from collections import deque


class Solution:
    def updateMatrix(self, matrix):
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        visited = [[set() for _ in range(n_cols)] for _ in range(n_rows)]
        queue = deque()
        dist_matrix = [[-1 for _ in range(n_cols)] for _ in range(n_rows)]
        for i in range(n_rows):
            for j in range(n_cols):
                if matrix[i][j] == 0:
                    queue.append((i, j))

        while queue:
            elem = queue.popleft()
            row, col = elem[0], elem[1]
            neighbors = []
            # up
            if row - 1 >= 0:
                neighbors.append((row - 1, col))
            # down
            if row + 1 < n_rows:
                neighbors.append((row + 1, col))
            # left
            if col - 1 >= 0:
                neighbors.append((row, col - 1))
            # right
            if col + 1 < n_cols:
                neighbors.append((row, col + 1))

            if matrix[row][col] == 0:
                dist_matrix[row][col] = 0
            else:
                dist_matrix[row][col] = 1 + min([dist_matrix[n[0]][n[1]] for n in neighbors if dist_matrix[n[0]][n[1]] != -1])

            for n in neighbors:
                if (row, col) not in visited[n[0]][n[1]]:
                    queue.append((n[0], n[1]))
                    visited[n[0]][n[1]].add((row, col))

        return dist_matrix




matrix = [[0, 0, 0],
          [0, 1, 0],
          [0, 0, 0]]

sol = Solution()
res = sol.updateMatrix(matrix)
for row in res:
    print(row)
print()

matrix = [[0, 0, 0],
          [0, 1, 0],
          [1, 1, 1]]


sol = Solution()
res = sol.updateMatrix(matrix)
for row in res:
    print(row)
