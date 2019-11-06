'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution:
    def generateParenthesis(self, n):
        result = []
        def generate(left_parens, right_parens, cur_str):
            if left_parens:
                generate(left_parens-1, right_parens, cur_str+'(')
            if right_parens > left_parens:
                generate(left_parens, right_parens-1, cur_str+')')
            if not right_parens:
                result.append(cur_str)

        
        result = []
        generate(n, n, '')
        return result

def isValid(s):
    stack = []
    open_chars = ['(', '[', '{']
    close_chars = [')', ']', '}']
    for char in s:
        if char in open_chars:
            stack.append(char)
        if char in close_chars:
            if not stack:
                return False
            else:
                match = stack.pop()
                if char == ')' and match != '(':
                    return False
                if char == ']' and match != '[':
                    return False
                if char == '}' and match != '{':
                    return False

    if len(stack) != 0:
        return False
    return True

sol = Solution()
for n in range(50):
    print(f'Input: {n}')
    print(f'Output: {(sol.generateParenthesis(n))}')
    print(f'Output: {isValid(sol.generateParenthesis(n))}')
