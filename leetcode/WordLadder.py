'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

from collections import deque
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_dict = {}
        for word in 

        '''
        #Time Limit Exceeded
        if endWord not in wordList:
            return 0
        def connected(word1, word2):
            count_diff = 0
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    if count_diff:
                        return False
                    count_diff += 1
            return True

        adj_list = {}
        adj_list[beginWord] = set()
        for word in wordList:
            adj_list[word] = set()

        n_words = len(wordList)
        for i in range(n_words):
            if connected(beginWord, wordList[i]):
                adj_list[beginWord].add(wordList[i])

        for i in range(n_words):
            cur_word = wordList[i]
            for j in range(n_words):
                if i != j:
                    if connected(cur_word, wordList[j]):
                        adj_list[cur_word].add(wordList[j])

        visited = {}
        visited[beginWord] = 0
        queue = deque()
        queue.append((beginWord, 1))
        while(queue):
            u, path_len = queue.popleft()
            for w in adj_list[u]:
                if w not in visited or visited[w] > path_len + 1:
                    visited[w] = path_len + 1
                    queue.append((w, path_len + 1))
        if endWord in visited:
            return visited[endWord]
        else:
            return 0
        '''


sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

print('Input')
print(f'beginWord = {beginWord}')
print(f'endWord = {endWord}')
print(f'wordList = {wordList}')
print(f'Output: {sol.ladderLength(beginWord, endWord, wordList)}')

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
print('Input')
print(f'beginWord = {beginWord}')
print(f'endWord = {endWord}')
print(f'wordList = {wordList}')
print(f'Output: {sol.ladderLength(beginWord, endWord, wordList)}')
