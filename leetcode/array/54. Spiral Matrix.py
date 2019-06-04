# coding=utf-8

"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []

        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1

        direction = 0  # 0 right, 1 down, 2 left, 3 up

        ans = []
        while True:
            if left > right or up > down:
                return ans

            if direction == 0:  # go right
                for i in range(left, right + 1):
                    ans.append(matrix[up][i])
                up += 1
            elif direction == 1:  # go down
                for i in range(up, down + 1):
                    ans.append(matrix[i][right])
                right -= 1
            elif direction == 2:  # go left
                for i in reversed(range(left, right + 1)):
                    ans.append(matrix[down][i])
                down -= 1
            else:  # go up
                for i in reversed(range(up, down + 1)):
                    ans.append(matrix[i][left])
                left += 1

            direction = (direction + 1) % 4
