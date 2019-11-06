'''
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
'''


class Solution:
    def numSquares(self, n):
        if n <= 1:
            return n
        squares = []
        i = 1
        square = i
        while(square <= n):
            square = i**2
            i += 1
            if square <= n:
                squares.append(square)
        num_squares = len(squares)
        dp = [0 for i in range(n + 1)]
        for i in range(1,n+1):
            min_num = dp[i - squares[0]] + 1
            j = 1
            while(j < num_squares):
                if i - squares[j] >= 0:
                    min_num = min(min_num, dp[i - squares[j]] + 1)
                j+= 1
            dp[i] = min_num
        return dp[n]



sol = Solution()
n = 6730
print(f'Input: {n}')
print(f'Output: {sol.numSquares(n)}')
