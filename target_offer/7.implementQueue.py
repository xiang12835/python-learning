# coding=utf-8


""" 题目描述

用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

"""


""" 思路解析
定义两个stack，分别是stack1和stack2，队列的push和pop是在两侧的，push操作很简单，只需要在stack1上操作，而pop操作时，先将stack1的所有元素push到stack2中，然后stack2的pop返回的元素即为目标元素，然后把stack2中的所有元素再push到stack1中。
"""


class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if not self.stack1:
            return None
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        r = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return r
