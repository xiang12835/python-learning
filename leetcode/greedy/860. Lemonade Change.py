# coding=utf-8


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        """
        贪心

        记录5和10的个数，如果有一个透支了，就说明不能满足找零

        T: O(n)
        S: O(1)
        """

        i = 0  # 5 美元的个数
        j = 0  # 10 美元的个数
        for bill in bills:
            if bill == 5:  # 付 5 美元
                i += 1
            elif bill == 10:  # 付 10 美元，找回 1 个 5 美元
                j += 1
                i -= 1
            else:  # 付 20 美元
                if j == 0:  # 付 20 美元，找回 3 个 5 美元
                    i -= 3
                else:  # 付 20 美元，找回 1 个 10 美元，1 个 5 美元
                    i -= 1
                    j -= 1

            if i < 0 or j < 0: # 易错，这个判断在for循环里
                return False

        return True
