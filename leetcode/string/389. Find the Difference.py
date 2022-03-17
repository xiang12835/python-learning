# coding=utf-8
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        """
        tc = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1})

        sc = Counter({'a': 1, 'b': 1, 'c': 1, 'd': 1})

        tc - sc = Counter({'e': 1})

        list(tc - sc) = ['e']
        """
        return list(Counter(t) - Counter(s))[0]