# coding=utf-8

"""

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

"""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int

        从前往后遍历字符串
一、入栈条件为1.栈为空 2.当前字符是'(' 3.栈顶符号位')'，因为三种条件都没办法消去成对的括号。
二、计算结果：符合消去成对括号时，拿当前下标减去栈顶下标即可

        """
        if not s:
            return 0

        stack = []
        ans = 0
        n = len(s)
        for i in range(n):
            # 入栈条件
            if not stack or s[i] == '(' or s[stack[-1]] == ')':
                stack.append(i)     # 下标入栈
            else:
                # 计算结果
                stack.pop()
                ans = max(ans, i - (stack[-1] if stack else -1))
        return ans

class Solution1(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        stack = [-1]
        ans = 0
        n = len(s)
        for i in range(n):
            # 入栈条件
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])
        return ans


if __name__ == "__main__":
    print Solution().longestValidParentheses(")()())")
