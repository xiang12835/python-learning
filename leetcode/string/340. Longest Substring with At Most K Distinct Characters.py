# coding=utf-8

"""
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.

"""


class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        import collections

        lookup = collections.defaultdict(int)
        fast, slow, counter, res = 0, 0, 0, 0
        n = len(s)
        while fast < n:
            lookup[s[fast]] += 1
            if lookup[s[fast]] == 1:
                counter += 1
            fast += 1   # fast 永远指向下一个待处理的字符
            while slow < fast and counter > k:
                lookup[s[slow]] -= 1
                if lookup[s[slow]] == 0:
                    counter -= 1
                slow += 1
            res = max(res, fast - slow)  # 因此这里是 fast - slow 而不是 fast - slow + 1
        return res


if __name__ == '__main__':
    s = "eceba"
    k = 2

    print Solution().lengthOfLongestSubstringKDistinct(s, k)
