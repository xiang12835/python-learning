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

        T：O(2^n)

        """
        self.l = []
        self._recursion(0, 0, n, "")
        return self.l

    def _recursion(self, left, right, n, result):

        # terminator
        if left == n and right == n:
            self.l.append(result)
            return

        # current

        # drill down
        if left < n:  # left 随时可以加，只要别超标
            self._recursion(left + 1, right, n, result + '(')

        if right < n and right < left:  # 右括号没用完，右括号要比左括号少
            self._recursion(left, right + 1, n, result + ')')

        # reverse


class Solution1(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.l = []
        self._gen(0, 2*n, "")
        return self.l

    def _gen(self, level, max, s):
        # terminator
        if level >= max:
            self.l.append(s)
            return

        # process current logic: left, right

        # drill down
        self._gen(level + 1, max, s + '(')
        self._gen(level + 1, max, s + ')')

        # reverse states
        # 局部变量，自己会清除，非全局变量，无需清除


if __name__ == "__main__":
    print Solution().generateParenthesis(2)
