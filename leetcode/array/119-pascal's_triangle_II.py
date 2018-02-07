"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        r = [1]
        for i in xrange(1, rowIndex + 1):
            r = list(map(lambda x, y: x + y, [0] + r, r + [0]))
        return r
