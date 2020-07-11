# coding=utf-8

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        l = ["()", "[]", "{}"]
        for i in xrange(0, len(s)):
            stack.append(s[i])
            if len(stack) >= 2 and stack[-2]+stack[-1] in l:
                stack.pop()
                stack.pop()
        return len(stack) == 0


class Solution2(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        d = {')':'(', ']':'[','}':'{'}

        for c in s:
            if c not in d:
                stack.append(c)
            elif not stack or d[c] != stack.pop():
                return False

        return not stack


class Solution3(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool

        方法：栈

        时间复杂度：O(n)O(n)，因为我们一次只遍历给定的字符串中的一个字符并在栈上进行 O(1)O(1) 的推入和弹出操作。
空间复杂度：O(n)O(n)，当我们将所有的开括号都推到栈上时以及在最糟糕的情况下，我们最终要把所有括号推到栈上。例如 ((((((((((。
        """
        stack = []
        d = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c not in d:  # 左刮号入栈
                stack.append(c)
            else:  # 右刮号，注意栈空
                val = stack.pop() if stack else '#'
                if d[c] != val:
                    return False

        return not stack


if __name__ == "__main__":
    s = Solution3()
    print s.isValid("(){}")
    print s.isValid("()a{}")
