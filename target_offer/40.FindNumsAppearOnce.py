# coding=utf-8


"""问题描述

一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。

"""


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        d = {}
        for n in array:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        r = []
        for k, v in d.items():
            if v == 1:
                r.append(k)

        return r
