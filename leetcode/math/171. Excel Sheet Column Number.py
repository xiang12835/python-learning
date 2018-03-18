"""
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
"""


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return reduce(lambda x, y: x * 26 + y, [ord(c) - 64 for c in list(s)])


if __name__ == "__main__":
    s = Solution()
    print s.titleToNumber("A")
    print s.titleToNumber("AA")
    print s.titleToNumber("AAA")
