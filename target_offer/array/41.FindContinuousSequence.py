# coding=utf-8


"""题目描述

小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

输出描述:

输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

"""


class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]

        滑动窗口：只有 右边界向右移动（扩大窗口） 和 左边界向右移动（缩小窗口） 两个操作

        左闭右开

        T: O(n)
        """
        start = 1
        end = 1
        s = 0

        ans = []
        while start <= target / 2:
            if s < target:  # 右移
                s += end
                end += 1
            elif s > target:  # 左移
                s -= start
                start += 1
            else:
                ans.append(range(start, end))
                s -= start
                start += 1
        return ans


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

""" 思路

设定两个指针，一个指向第一个数，一个指向最后一个数，在此之前需要设定第一个数和最后一个数的值，由于是正数序列，所以可以把第一个数设为1，最后一个数为2（因为是要求是连续正数序列，最后不可能和第一个数重合）。下一步就是不断改变第一个数和最后一个数的值，如果从第一个数到最后一个数的和刚好是要求的和，那么把所有的数都添加到一个序列中；

如果大于要求的和，则说明从第一个数到最后一个数之间的范围太大，因此减小范围，需要把第一个数的值加1，同时把当前和减去原来的第一个数的值；

如果小于要求的和，说明范围太小，因此把最后一个数加1，同时把当前的和加上改变之后的最后一个数的值。这样，不断修改第一个数和最后一个数的值，就能确定所有连续正数序列的和等于S的序列了。

"""


class Solution2:
    def FindContinuousSequence(self, tsum):
        # write code here
        result = []
        start, end = 1, 2
        while start < end:
            curSum = (start + end) * (start - end + 1) / 2
            if curSum == tsum:
                tmp = []
                for i in range(start, end+1):
                    tmp.append(i)
                result.append(tmp)
                start += 1
            elif curSum < tsum:
                end += 1
            else:
                start += 1
        return result
