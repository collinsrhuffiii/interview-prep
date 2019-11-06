'''

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_elem = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(0)
            self.min_elem = x
        else:
            self.stack.append(x - self.min_elem)
            self.min_elem = min(self.min_elem, x)
        

    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return None

        pop_val = self.stack.pop()
        if pop_val < 0:
            self.min_elem = self.min_elem - pop_val

        

    def top(self):
        """
        :rtype: int
        """
        top = self.stack[-1]
        if top > 0:
            return top+self.min_elem
        else:
            return self.min_elem
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_elem
