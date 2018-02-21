# coding=utf-8


""" 问题描述

我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？


"""


""" 思路解析

我们用f(n)表示覆盖2*n的矩形的方法数。
可以看出，f(1)=1;f(2)=2。
那么，假设到了n，那么上一步就有两种情况，在n-1的时候，竖放一个矩形，或着是在n-2时，横放两个矩形（这里不能竖放两个矩形，因为放一个就变成了n-1，那样情况就重复了），所以总数是f(n)=f(n-1)+f(n-2)。

反向思考，但是编写代码的时候要正向求解，首先根据f(1)和f(2)计算出f(3),再根据f(2)和f(3)计算出f(4)…..一次类推计算出第n项。很容易理解这种思路的时间复杂度是O(n).

"""


class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2

        l = [1, 2]
        for i in xrange(3, number + 1):
            l.append(l[-2] + l[-1])

        return l[-1]
