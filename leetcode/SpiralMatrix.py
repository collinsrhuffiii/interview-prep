'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''

class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        sentinel = '0'
        direction_map = [(0,1), (1,0), (0,-1), (-1,0)]
        def flood(i,j,direction):
            if i >= rows or i <= -1 or j >= cols or j <= -1 or matrix[i][j] == sentinel:
                return (direction+1)%4
            result.append(matrix[i][j])
            matrix[i][j] = sentinel
            move = direction_map[direction]
            direction = flood(i+move[0],j+move[1],direction)
            move = direction_map[direction]
            flood(i+move[0],j+move[1],direction)
            return direction
        flood(0,0,0)
        return result
        '''
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        result = []
        sentinel = '0'
        direction_map = [(0,1), (1,0), (0,-1), (-1,0)]
        def flood(i,j,direction):
            print(i,j,matrix[i][j])
            result.append(matrix[i][j])
            matrix[i][j] = sentinel
            change_dir = True
            i = 0
            while(change_dir and i < 4):
                move = direction_map[direction]
                new_vert_pos = i+move[0]
                new_horiz_pos = j+move[1]
                change_dir = False
                if new_vert_pos >= rows or new_vert_pos <= -1:
                    change_dir = True
                elif new_horiz_pos >= cols or new_horiz_pos <= -1:
                    change_dir = True
                elif grid[new_vert_pos][new_horiz_pos] == sentinel:
                    change_dir = True
                if change_dir:
                    direction = (direction+1)%4
                i += 1

            if i == 4:
                return
            else:
                move = direction_map[direction]
                new_vert_pos = i+move[0]
                new_horiz_pos = j+move[1]
                flood(new_vert_pos, new_horiz_pos, direction)


        flood(0,0,0)
        return result
        '''

sol = Solution()
grid = [ [1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12] ]
print(f'Input:')
for row in grid:
    print(row)
print(f'Output: {sol.spiralOrder(grid)}')

grid = [ [1, 2, 3, 4], [5, 6, 7, 8], [9,10,11,12],[13,14,15,16],[17,18,19,20]]
print(f'Input:')
for row in grid:
    print(row)
print(f'Output: {sol.spiralOrder(grid)}')
