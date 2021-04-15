# coding=utf-8

'''
Given an input string, reverse the string word by word.



Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.


Follow up:

For C programmers, try to solve it in-place in O(1) extra space.

'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        if not s:
            return s

        reversed_s = s[::-1]
        ans = []
        for w in reversed_s.split(' '):
            if not w:
                continue
            ans.append(w[::-1])

        return ' '.join(ans)


class Solution1:
    def reverseWords(self, s: str) -> str:
        s = s.strip()

        words = s[::-1].split(' ')
        r = []
        for word in words:
            if word:
                r.append(word[::-1])

        return ' '.join(r)


class Solution2(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.strip().split(' ')))
