# coding=utf-8

""" 题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""


class Solution:
    def reOrderArray(self, array):
        # write code here
        odd_list = []
        even_list = []
        for v in array:
            if v % 2 == 1:
                odd_list.append(v)
            else:
                even_list.append(v)
        return odd_list+even_list


class Solution1:
    def reOrderArray(self, array):
        # write code here
        array.sort(key=lambda v: v % 2, reverse=True)
        return array


if __name__ == "__main__":
    s = Solution()
    print s.reOrderArray([1,2,3,4,5])
    s1 = Solution1()
    print s1.reOrderArray([1,2,3,4,5])
