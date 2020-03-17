# coding=utf-8

"""
How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in 0(1) time.

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> return -3.
minStack.pop();
minStack.top();      --> return 0.
minStack.getMin();   --> return -2.
"""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.

        双栈，多定义一个栈，用来存储最小值

        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        cur_min = self.getMin()
        if not self.min_stack or x < cur_min:
            self.min_stack.append(x)
        else:
            self.min_stack.append(cur_min)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
        if self.min_stack:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_stack:
            return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

