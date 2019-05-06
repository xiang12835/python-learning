"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

"""


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int


        0 [7, 1, 8, 3]
        1 [7, 6, 8, 3]
        2 [7, 6, 10, 3]
        0 [9, 6, 10, 3]
        1 [9, 10, 10, 3]
        0 [11, 10, 10, 3]
        11

        """
        if not triangle:
            return 0

        res = triangle[-1]
        for i in xrange(len(triangle) - 2, -1, -1):
            for j in xrange(len(triangle[i])):
                res[j] = min(res[j], res[j + 1]) + triangle[i][j]

                # print j, res
        return res[0]


if __name__ == "__main__":
    s = Solution()
    print s.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])
