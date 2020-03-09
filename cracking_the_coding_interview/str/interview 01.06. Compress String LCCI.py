# coding=utf-8

"""

Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).

Example 1:

Input: "aabcccccaaa"
Output: "a2b1c5a3"
Example 2:

Input: "abbccd"
Output: "abbccd"
Explanation:
The compressed string is "a1b2c2d1", which is longer than the original string.

"""

import itertools
class Solution(object):
    def compressString(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = ''
        for c, v in itertools.groupby(S):
            s += c + str(len(list(v)))
        return s if len(s) < len(S) else S

if __name__ == '__main__':
    ss = 'aabcccccaaa'
    print Solution().compressString(ss)



