'''
1161. Maximum Level Sum of a Binary Tree
Medium

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level X such that the sum of all the values of nodes at level X is maximal.

 

Example 1:

Input: [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

 

Note:

    The number of nodes in the given tree is between 1 and 10^4.
    -10^5 <= node.val <= 10^5
'''

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level_sums = []
        queue = deque()
        queue.append((root, 0))
        while queue:
            # BFS
            cur_node, level = queue.popleft()
            if cur_node is None:
                continue
               
            if len(level_sums) <= level:
                level_sums.append(0)

            level_sums[level] += cur_node.val
            queue.append((cur_node.left, level + 1))
            queue.append((cur_node.right, level + 1))

        max_level = 0
        max_level_sum = 0
        for i, level_sum in enumerate(level_sums):
            if level_sum > max_level_sum:
                max_level = i
                max_level_sum = level_sum

        return max_level + 1
