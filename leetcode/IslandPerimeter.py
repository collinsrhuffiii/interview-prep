'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
'''

class Solution:
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        def flood(i,j):
            if i >= rows or i <= -1 or j >= cols or j <= -1 or grid[i][j] == 0:
                return 1
            if grid[i][j] == -1:
                return 0
            grid[i][j] = -1
            count = flood(i+1, j) + flood(i-1, j) + flood(i, j+1) + flood(i, j-1)
            return count

        b = False
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    b = True
                    count = flood(i,j)
                    break
            if b:
                break
        return count
