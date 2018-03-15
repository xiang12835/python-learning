"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

import os


class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        return os.path.commonprefix(strs)


class Solution1(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        print zip(*strs)
        for z in zip(*strs):
            bag = set(z)
            if len(bag) == 1:
                prefix += bag.pop()
            else:
                break
        return prefix


if __name__ == "__main__":
    s = Solution1()
    print s.longestCommonPrefix(["abc", "ab", "abcdef"])
