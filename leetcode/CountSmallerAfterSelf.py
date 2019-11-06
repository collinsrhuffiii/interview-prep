'''
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
'''
class Solution:
    def countSmaller(self, nums):
        if not nums:
            return []
        count = [0 for _ in range(len(nums))]
        def mergeSort(nums):
            n = len(nums)
            if n == 1:
                return nums
            left,right = mergeSort(nums[:n//2]), mergeSort(nums[n//2:])
            res = [0 for _ in range(n)]
            i = n-1
            for i in range(n)[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    count[left[-1][0]] += len(right)
                    res[i] = left.pop()
                else:
                    res[i] = right.pop()
            return res

        nums = mergeSort(list(enumerate(nums)))
        print(nums)
        return count
'''
class Node:
    def __init__(self, val):
        self.val = val
        self.count = 0
        self.duplicate = 1
        self.left = None
        self.right = None

def insert(node, val, count, ans, index):
    if node == None:
        node = Node(val)
        ans[index] = count
    elif node.val == val:
        node.duplicate += 1
        ans[index] = (count + node.count)
    elif node.val > val:
        node.count += 1
        node.left = insert(node.left, val, count, ans, index)
    else:
        node.right = insert(node.right, val, count + node.duplicate + node.count,
                ans, index)
    return node


class Solution:
    def countSmaller(self, nums):
        if not nums:
            return []
        n = len(nums)
        root = Node(nums[n-1])
        count = [0 for _ in range(n)]
        for i in range(n-2, -1, -1):
            insert(root, nums[i], 0, count, i)
        return count

        Time Limit Exceeded
        n = len(nums)
        count = [0 for _ in range(n)]
        for i in range(n):
            cur_count = 0
            cur_num = nums[i]
            for j in range(i,n):
                if cur_num > nums[j]:
                    cur_count += 1
            count[i] = cur_count
        return count
'''
sol = Solution()
nums = [2,0,1]
print(f'Input: {nums}')
print(f'Output: {sol.countSmaller(nums)}')

nums = [5,2,6,1]
print(f'Input: {nums}')
print(f'Output: {sol.countSmaller(nums)}')
