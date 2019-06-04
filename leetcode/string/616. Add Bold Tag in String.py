# coding=utf-8

"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:
Input:
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input:
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
"""


class Solution(object):
    def addBoldTag(self, s, words):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        lookup = [0] * len(s)
        for d in words:
            pos = s.find(d)
            while pos != -1:
                lookup[pos:pos+len(d)] = [1] * len(d)
                pos = s.find(d, pos + 1)

        result = []
        for i in xrange(len(s)):
            if lookup[i] and (i == 0 or not lookup[i-1]):
                result.append("<b>")
            result.append(s[i])
            if lookup[i] and (i == len(s)-1 or not lookup[i+1]):
                result.append("</b>")
        return "".join(result)


if __name__ == '__main__':
    # s = "abcxyz123"
    # words = ["abc", "123"]

    s = "aaabbcc"
    words = ["aaa", "aab", "bc"]

    print Solution().addBoldTag(s, words)
