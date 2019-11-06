'''
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
'''

class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(i,j):
            if i >= rows or j >= cols or i < 0 or j < 0 or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    dfs(i,j)
                    islands += 1
        return islands

        '''
        Time limit exceeded
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        unvisited = set() 
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    unvisited.add((i,j))
        
        def bfs(i,j):
            queue = []
            queue.append((i,j))
            unvisited.add((i,j))
            while(queue):
                v = queue.pop(0)
                if v in unvisited:
                    unvisited.remove((v[0],v[1]))
                up = down = left = right = (v[0], v[1])
                if v[0]+1 < rows:
                    up = (v[0]+1, v[1])
                if v[1]+1 < cols:
                    right = (v[0], v[1]+1)
                if v[0]-1 >= 0:
                    down = (v[0]-1, v[1])
                if v[1]-1 >= 0:
                    left = (v[0], v[1]-1)
                adjs = [up, down, left, right]
                for adj in adjs:
                    if adj in unvisited and grid[adj[0]][adj[1]] == '1':
                        queue.append(adj)

        islands = 0
        while(unvisited):
            islands += 1
            start = unvisited.pop()
            bfs(start[0], start[1])

        return islands
        '''

sol = Solution()
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print('Input')
for row in grid:
    print(row)
print(f'Output = {sol.numIslands(grid)}')
