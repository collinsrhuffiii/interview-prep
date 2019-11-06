'''
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

class Solution:
    def reconstructQueue(self, people):
        if not people:
            return []
        num_people = len(people)
        people = sorted(people, key=lambda x:x[1])
        sorted_height = sorted(people, reverse=True, key=lambda x:x[0])
        res = []
        tallest = sorted_height[0]
        res.append(tallest)
        i = 1
        while(i < num_people and sorted_height[i][0] == tallest[0]):
            res.append(sorted_height[i])
            i += 1
        while(i < num_people):
            res.insert(sorted_height[i][1], sorted_height[i])
            i += 1
        return res




sol = Solution()
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(f'Input: {people}')
print(f'Output: {sol.reconstructQueue(people)}')
