'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''


class Solution:
    def coinChange(self, coins, amount):
        dp = [-1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(1,amount+1):
            min_coins = -1
            for coin in coins:
                if coin <= i:
                    sub_res = dp[i - coin]
                    if sub_res != -1:
                        if min_coins == -1:
                            min_coins = sub_res + 1
                        else:
                            min_coins = min(min_coins, sub_res+1)
            dp[i] = min_coins
        return dp[amount]

sol = Solution()
coins = [1,2,5]
amount = 11
print(f'Input: coins = {coins}, amount = {amount}')
print(f'Output: {sol.coinChange(coins, amount)}')


coins = [2]
amount = 3
print(f'Input: coins = {coins}, amount = {amount}')
print(f'Output: {sol.coinChange(coins, amount)}')
