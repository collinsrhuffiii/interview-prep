'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

class Solution:
    def letterCombinations(self, digits):
        '''
        DFS
        '''

        letters_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno','7':'pqrs','8':'tuv', '9':'wxyz'}

        def dfs(digits, current, result):
            if not digits:
                result.append(current)
                return
            else:
                for c in letters_map[digits[0]]:
                    dfs(digits[1:], current+c, result)
        
        if not digits:
            return []

        combinations = []
        dfs(digits, '', combinations)
        return combinations

        '''
        BFS
        combinations = []
        if not digits:
            return combinations
        num_digits = len(digits)
        letters = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        combinations.append('')
        for i in range(num_digits):
            cur_dig = int(digits[i])
            while(len(combinations[0]) == i):
                t = combinations.pop(0)
                for s in letters[cur_dig]:
                    combinations.append(t+s)
        return combinations
        '''




            


sol = Solution()
digits = '23'
print(f'Input: {digits}')
print(f'Output: {(sol.letterCombinations(digits))}')

