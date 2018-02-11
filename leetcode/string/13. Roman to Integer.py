"""
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # VIII - 8 | IV - 4
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        r = 0
        for i in xrange(len(s) - 1):
            first = s[i]
            second = s[i + 1]
            if d[first] < d[second]:
                r -= d[s[i]]
            else:
                r += d[s[i]]
        r += d[s[-1]]
        return r
