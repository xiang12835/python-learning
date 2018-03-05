# -*- coding:utf-8 -*-


""" 题目描述
LL今天心情特别好,因为他去买了一副扑克牌,发现里面居然有2个大王,2个小王(一副牌原本是54张^_^)...他随机从中抽出了5张牌,想测测自己的手气,看看能不能抽到顺子,如果抽到的话,他决定去买体育彩票,嘿嘿！！“红心A,黑桃3,小王,大王,方片5”,“Oh My God!”不是顺子.....LL不高兴了,他想了想,决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。上面的5张牌就可以变成“1,2,3,4,5”(大小王分别看作2和4),“So Lucky!”。LL决定去买体育彩票啦。 现在,要求你使用这幅牌模拟上面的过程,然后告诉我们LL的运气如何。为了方便起见,你可以认为大小王是0。
"""


""" 思路解析
1、排序 
2、计算所有相邻数字间隔总数 
3、计算0的个数 
4、如果2、3相等，就是顺子 
5、如果出现对子，则不是顺子
"""


class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return False
        numbers = sorted(numbers)
        gap_count = 0
        zero_count = 0
        for n in numbers:
            if n == 0:
                zero_count += 1

        numbers = numbers[zero_count:]
        if len(numbers) != len(set(numbers)):
            return False
        if len(numbers) == 1:
            return True

        small = 0
        big = 1
        while big <= len(numbers) - 1:
            diff = numbers[big] - numbers[small]
            gap_count += diff - 1
            small += 1
            big += 1

        if gap_count == zero_count:
            return True


if __name__ == "__main__":
    s = Solution()
    # print s.IsContinuous([1,3,2,5,4])
    # print s.IsContinuous([0,1,3,5,0])
    print s.IsContinuous([3,0,0,0,0])
