# coding=utf-8


"""题目描述

在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

"""


class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        for i in xrange(len(numbers)):
            for j in xrange(i+1, len(numbers)):
                if numbers[i] == numbers[j]:
                    duplication.append(numbers[i])
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    print s.duplicate([2,1,3,1,4],duplication=[])
