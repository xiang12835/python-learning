# coding=utf-8
"""
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]

class Solution1(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str

        return s[::-1]

        """

        def recursion(left, right):
            """
            T：O(N)，执行了 N/2 次的交换。
            S：O(N)，递归过程中使用的堆栈空间。
            """
            if left >= right:
                return
            s[left], s[right] = s[right], s[left]
            recursion(left + 1, right - 1)

        recursion(0, len(s) - 1)



class Solution2(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        左右对撞

        T：O(N)。执行了 N/2 次的交换。
        S：O(1)，只使用了常数级空间。
        """

        ss = list(s)
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            ss[l], ss[r] = ss[r], ss[l]
            l += 1
            r -= 1

        return ''.join(ss)
