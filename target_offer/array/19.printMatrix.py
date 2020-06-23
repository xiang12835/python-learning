# coding=utf-8


"""题目描述

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，例如，如果输入如下矩阵： 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10
"""


class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        """
        思路：可以将矩阵看成若干层，首先打印最外层的元素，其次打印次外层的元素，直到打印最内层的元素。
        T：O(mn)，其中 mm 和 nn 分别是输入矩阵的行数和列数。矩阵中的每个元素都要被访问一次。
        S：O(1)。除了输出数组以外，空间复杂度是常数。

        :param matrix:
        :return:
        """
        # write code here
        if not matrix:
            return []

        left = 0
        right = len(matrix[0]) - 1
        up = 0
        down = len(matrix) - 1

        direction = 0  # 0 right, 1 down, 2 left, 3 up

        r = []
        while True:
            if left > right or up > down:
                return r

            if direction == 0:  # go right
                for i in range(left, right + 1):
                    r.append(matrix[up][i])
                up += 1

            if direction == 1:  # go down
                for i in range(up, down + 1):
                    r.append(matrix[i][right])
                right -= 1

            if direction == 2:  # go left
                for i in reversed(range(left, right + 1)):
                    r.append(matrix[down][i])
                down -= 1

            if direction == 3:  # go up
                for i in reversed(range(up, down + 1)):
                    r.append(matrix[i][left])
                left += 1

            direction = (direction + 1) % 4



