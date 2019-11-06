'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s):
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
s = "()"
print(f'Input: {s}')
print(f'Output: {sol.isValid(s)}')

s = "()[]{}"
print(f'Input: {s}')
print(f'Output: {sol.isValid(s)}')

s = "(]"
print(f'Input: {s}')
print(f'Output: {sol.isValid(s)}')

s = "([)]"
print(f'Input: {s}')
print(f'Output: {sol.isValid(s)}')

s = "{[]}"
print(f'Input: {s}')
print(f'Output: {sol.isValid(s)}')
