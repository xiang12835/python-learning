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


if __name__ == "__main__":
    s = Solution()
    print s.isValid("(){}")
    print s.isValid("()a{}")
