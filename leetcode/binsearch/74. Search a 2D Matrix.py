# coding=utf-8

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        二分查找

        T: O(logMN)
        S: O(1)
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        l = 0
        r = m * n - 1

        while l <= r:
            mid = l + (r - l) // 2
            mid_val = matrix[mid // n][mid % n]
            if target == mid_val:
                return True
            elif target > mid_val:
                l = mid + 1
            else:
                r = mid - 1
        return False
