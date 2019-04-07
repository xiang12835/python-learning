# coding=utf-8


"""

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]

        left 已经使用了的左括号的个数
        right 已经使用了的右括号的个数

        """
        self.l = []
        self._gen(0, 0, n, "")
        return self.l

    def _gen(self, left, right, n, result):
        if left == n and right == n:
            self.l.append(result)
            return

        if left < n:
            self._gen(left + 1, right, n, result + '(')

        if right < n and right < left:
            self._gen(left, right + 1, n, result + ')')
