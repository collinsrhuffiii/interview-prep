'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number is higher or lower.

You call a pre-defined API guess(int num) which returns 3 possible results (-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.

Return 6.
'''

class Solution(object):
    def guessNumber(self, n):
        if n == 1:
            return 1
        high = n
        low = 0
        mid = (high+low)//2
        while(low <= high):
            mid = (high+low)//2
            res = guess(mid)
            if res == 0:
                return mid
            elif res == -1:
                high = mid-1
            else:
                low = mid+1
        return -1
