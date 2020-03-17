# coding=utf-8

"""
Implement a MyQueue class which implements a queue using two stacks.

 
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);
queue.peek();  // return 1
queue.pop();   // return 1
queue.empty(); // return false
"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        r = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return r

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        r = self.stack2[-1]
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return r

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack1 and not self.stack2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
