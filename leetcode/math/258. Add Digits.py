# coding=utf-8

class Solution:
    def addDigits(self, num: int) -> int:
        """
        数学归纳
        """
        if num > 9:
            num = num % 9
            if num == 0:
                return 9
            return num
        else:
            return num
