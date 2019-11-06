'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
'''


class Solution:
    def evalRPN(self, tokens):
        def perform_operation(operation, x, y):
            if operation == '+':
                return x+y
            if operation == '-':
                return x-y
            if operation == '*':
                return x*y
            if operation == '/':
                return x/y

        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token in operators:
                operand2 = int(stack.pop())
                operand1 = int(stack.pop())
                result = perform_operation(token, operand1, operand2)
                stack.append(result)
            else:
                stack.append(token)
        return int(stack[0])

sol = Solution()
tokens = ["4", "13", "5", "/", "+"]
print(f'Input: {tokens}')
print(f'Output: {sol.evalRPN(tokens)}')
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(f'Input: {tokens}')
print(f'Output: {sol.evalRPN(tokens)}')
