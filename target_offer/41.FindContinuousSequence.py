# coding=utf-8


"""题目描述

小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

输出描述:

输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

"""


class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        start = 1
        end = 2
        cur_sum = start + end
        r = []
        while start <= tsum/2:
            if cur_sum < tsum:
                end += 1
                cur_sum += start
            elif cur_sum > tsum:
                start -= 1
                cur_sum -= start
            else:
                r.append(range(start, end+1))
                end += 1
                cur_sum += start
        return r


class Solution1:
    def FindContinuousSequence(self, tsum):
        # write code here
        l = [1, 2]
        r = []
        while len(l) > 1:
            if sum(l) < tsum:
                l.append(l[-1]+1)
            elif sum(l) > tsum:
                l.pop(0)
            else:
                r.append(l[:])
                l.pop(0)
        return r
