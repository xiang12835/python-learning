# coding=utf-8


"""问题描述

输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。

"""


"""思路解析

这道题其实希望我们能够找到一个排序规则，数组根据这个规则排序之后能排成一个最小的数字。要确定排序的规则，就要比较两个数字，也就是给出两个数字m和n，我们需要确定一个规则判断m和n哪个应该排在前面，而不是仅仅比较这两个数字的值哪个更大。

根据题目的要求，两个数字m和n能拼接称数字mn和nm。如果mn<nm，那么我们应该打印出mn，也就是m应该拍在n的前面，我们定义此时m小于n；反之，如果nm<mn，我们定义n小于m。如果mn=nm,m等于n。

"""


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        l = [str(n) for n in numbers]
        l.sort(lambda x,y : cmp(x+y, y+x))
        return "".join(l)
