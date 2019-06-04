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
        l, r, counter, res = 0, 0, 0, 0
        while r < len(s):
            lookup[s[r]] += 1
            if lookup[s[r]] == 1:
                counter += 1
            r += 1   # end 永远指向下一个待处理的字符
            while l < r and counter > k:
                lookup[s[l]] -= 1
                if lookup[s[l]] == 0:
                    counter -= 1
                l += 1
            res = max(res, r - l)  # 因此这里是r-l而不是r-l+1
        return res


if __name__ == '__main__':
    s = "eceba"
    k = 2

    print Solution().lengthOfLongestSubstringKDistinct(s, k)
