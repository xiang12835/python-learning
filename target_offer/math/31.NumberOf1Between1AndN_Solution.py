# coding=utf-8

"""题目描述

求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数。

"""


"""思路解析
将1-n全部转换为字符串
只需要统计每个字符串中'1'出现的次数并相加即可
"""


class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        count = 0
        for i in xrange(1, n+1):
            for c in str(i):
                if "1" == c:
                    count += 1
        return count
