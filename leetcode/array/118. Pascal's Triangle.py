"""
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        r = [[1]]
        for i in xrange(1, numRows):
            r.append(map(lambda x, y: x + y, [0] + r[-1], r[-1] + [0]))
        return r


class Solution1(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        r = [[1]]
        for i in range(1, numRows):
            first_list = [0] + r[-1]
            second_list = r[-1] + [0]
            l = map(lambda x, y: x + y, first_list, second_list)
            r.append(l)

        return r

if __name__ == "__main__":
    s = Solution()
    print s.generate(4)

