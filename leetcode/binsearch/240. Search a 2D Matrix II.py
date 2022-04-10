# coding=utf-8

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """

        法一：直接查找

        T: O(mn)
        S: O(1)

        法二：二分查找

        T：O(mlogn)。对一行使用二分查找的时间复杂度为 O(logn)，最多需要进行 m 次二分查找。
        S：O(1)。

        法三：从右上角考虑

        T: O(max(M,N))，因为每次都会往下或者往左走
        S: O(1)
        """
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])

        i = 0
        j = n - 1

        while i < m and j >= 0:
            if target > matrix[i][j]:
                i += 1
            elif target < matrix[i][j]:
                j -= 1
            else:
                return True

        return False