"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

import os


class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):
        return os.path.commonprefix(strs)