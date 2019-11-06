'''

'''

from collections import deque

class Solution:
    def hasPath(self, maze, start, dest):
        rows = len(maze)
        cols = len(maze[0])

        visited = [[False for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        queue.appendleft(start)
        visited[start[0]][start[1]] = True
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while(queue):
            s = queue.pop()
            if s[0] == dest[0] and s[1] == dest[1]:
                return True
            for direction in directions:
                x = s[0] + direction[0]
                y = s[1] + direction[1]
                while x >= 0 and y >= 0 and x < rows and y < cols and maze[x][y] == 0:
                    x += direction[0]
                    y += direction[1]
                if not visited[x-direction[0]][y-direction[1]]:
                    queue.appendleft((x-direction[0],y-direction[1]))
                    visited[x-direction[0]][y-direction[1]] = True
        return False



sol = Solution()
maze = [
        [0,0,0],
        [0,0,0]]
start = (0,0)
dest = (1, 2)
print(sol.hasPath(maze, start, dest))
start = (0, 4)
dest = (4,4)
maze = [ 
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,0,1,0],
    [1,1,0,1,1],
    [0,0,0,0,0]]

print(sol.hasPath(maze, start, dest))

maze = [
    [0,0,1,0,0],
    [0,0,0,0,0],
    [0,0,0,1,0],
    [1,1,0,1,1],
    [0,0,0,0,0]]

start = (0,4)
dest = (3,2)
print(sol.hasPath(maze, start, dest))
