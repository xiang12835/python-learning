# coding=utf-8

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        二分查找

        T: O(x)
        S: O(1)
        """
        l = 0
        r = num

        while l <= r:  # 易错，有等于号
            mid = l + (r - l) // 2  # 易错
            if mid * mid == num:
                return True
            elif mid * mid > num:
                r = mid - 1  # 易错
            else:
                l = mid + 1

        return False
