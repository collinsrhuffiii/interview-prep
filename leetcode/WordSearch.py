'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def search(word_to_find, row, col, visited):
            visited = set(visited)
            visited.add((row, col))
            if (row < 0 or row >= rows or col < 0 or col >= cols or
                    word_to_find[0] != board[row][col]):
                return False
            
            if len(word_to_find) == 1 and word_to_find[0] == board[row][col]:
                return True
        
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if (new_row, new_col) not in visited:
                    result = search(word_to_find[1:], new_row, new_col, visited)
                    if result == True:
                        return True
            return False


        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if search(word, row, col, set()):
                        return True
        return False


sol = Solution()
'''
board = [['A','B','C','E'],
         ['S','F','C','S'],
         ['A','D','E','E']]

word = 'ABCCED'
print(f'Input: {word}')
print(f'Output: {sol.exist(board, word)}')
word = 'SEE'
print(f'Input: {word}')
print(f'Output: {sol.exist(board, word)}')
word = 'ABCB'
print(f'Input: {word}')
print(f'Output: {sol.exist(board, word)}')
'''

board = [['a','b'],
         ['c','d']]
word = 'cdba'
print(f'Input: {word}')
print(f'Output: {sol.exist(board, word)}')
