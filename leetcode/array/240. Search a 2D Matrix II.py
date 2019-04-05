# coding=utf-8

"""

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.

"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        row = len(matrix)
        column = len(matrix[0]) if row else 0

        for i in xrange(row):
            for j in xrange(column):
                if matrix[i][j] == target:
                    return True

        return False


class Solution1(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        时间复杂度O(max(M,N))，因为每次都会往下或者往左走

        """
        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0]) if row else 0

        i = 0
        j = col - 1

        while i < row and j >= 0:
            if matrix[i][j] < target:
                i += 1
            elif matrix[i][j] > target:
                j -= 1
            else:
                return True

        return False
