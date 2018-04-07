"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

"""


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        se = set()
        for c in s:
            if c not in se:
                se.add(c)
            else:
                se.remove(c)
        if len(se) > 0:
            return len(s) - len(se) + 1
        else:
            return len(s)


if __name__ == "__main__":
    s = Solution()
    print s.longestPalindrome("abcccccdd")
