"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.



Requirements for atoi:

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

"""


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        INT_MAX = 2147483647
        INT_MIN = -2147483648

        s = str.strip()
        sign = 1
        if not s:
            return 0
        if s[0] in ["+", "-"]:
            if s[0] == "-":
                sign = -1
            s = s[1:]
        r = 0
        for c in s:
            if c.isdigit():
                r = r * 10 + int(c)
            else:
                break
        r *= sign
        if r > INT_MAX:
            return INT_MAX
        if r < INT_MIN:
            return INT_MIN

        return r


if __name__ == "__main__":
    s = Solution()
    print s.myAtoi("  -0012a42")
    print s.myAtoi("+-1")
    print s.myAtoi("-+1")
    print s.myAtoi("--1")
    print s.myAtoi("abc")

