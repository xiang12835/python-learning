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


class Solution1(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int

        将数字转成字符串，在求和

        """
        ss = str(num)
        while (len(ss) > 1):
            tmp = 0
            for c in ss:
                tmp += int(c)
            ss = str(tmp)
        return int(ss)
