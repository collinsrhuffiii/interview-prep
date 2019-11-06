'''
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
'''
import random

class Solution:
    def __init__(self, nums):
        self.nums = nums
        self.n = len(nums)

    def reset(self):
        return self.nums

    def shuffle(self):
        shuffled = self.nums
        for i in range(self.n):
            j = random.randint(i, self.n-1)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled
