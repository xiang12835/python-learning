# coding=utf-8

"""

Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False

"""


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        滑动窗口
        我们说了，不要关注排列的形式，而是关注排列中元素的数量关系，比如aab，那么，转换为数量关系就是{a:2,b:1}，因为S1长度为3，所以我们的窗口长度也为3，如果我们在S2的找到了这样一个窗口符合出现a的次数是两个，b是一个，那么S2就是包含S1的排列的。
        """
        if len(s1) > len(s2):
            return False

        d = self._gen_count(s1)

        s = 0
        e = len(s1)
        while e <= len(s2) + 1:
            tmp_str = s2[s:e]
            tmp_d = self._gen_count(tmp_str)
            if tmp_d == d:
                return True

            s += 1
            e += 1

        return False

    def _gen_count(self, s):
        _dict = {}
        for c in s:
            if c in _dict:
                _dict[c] += 1
            else:
                _dict[c] = 1
        return _dict


class Solution1(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        sorted_list = sorted(list(s1))
        s = 0
        e = len(s1)
        while e <= len(s2) + 1:
            tmp_str = s2[s:e]
            tmp_list = sorted(list(tmp_str))
            if tmp_list == sorted_list:
                return True

            s += 1
            e += 1

        return False


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"

    # s1 = "abc"
    # s2 = "bbbca"
    print Solution1().checkInclusion(s1, s2)
