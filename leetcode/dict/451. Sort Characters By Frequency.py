# coding=utf-8

"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
"""


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for c in list(s):
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        items = d.items()
        sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
        r = []
        for k, v in sorted_items:
            for _ in xrange(v):
                r.append(k)
        return ''.join(r)


if __name__ == '__main__':
    s = "tree"
    r = Solution().frequencySort(s)
    print r
