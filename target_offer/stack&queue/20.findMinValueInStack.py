# coding=utf-8


"""题目描述

定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。

"""


class Solution:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        min_node = self.min()
        if not self.min_stack or node < min_node:
            self.min_stack.append(node)
        else:
            self.min_stack.append(min_node)

    def pop(self):
        # write code here
        if self.stack:
            self.stack.pop()
        if self.min_stack:
            self.min_stack.pop()

    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]

    def min(self):
        # write code here
        if self.min_stack:
            return self.min_stack[-1]
