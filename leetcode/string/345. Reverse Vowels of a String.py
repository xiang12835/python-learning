"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel_str = "aeiou"
        length = len(s)
        l = 0
        r = length - 1
        while l < r:
            while s[l] not in vowel_str:
                l += 1
            while s[r] not in vowel_str:
                r -= 1


