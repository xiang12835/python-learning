# coding=utf-8

"""

1、给定一个字符串，找出不含有重复字符的最长子串的长度。
Given a string, find the length of the longest substring without repeating characters.

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # 快慢指针

        if not s:
            return 0

        fast = 0
        slow = 0

        r = 0

        ss = set()
        while fast < len(s) and slow < len(s):
            if s[fast] not in ss:
                ss.add(s[fast])

                r = max(r, fast - slow + 1)

                fast += 1

                print s[slow:fast]

            else:
                ss.discard(s[slow])
                slow += 1

        return r


if __name__ == "__main__":
    s = "abcabcbb"
    print Solution().lengthOfLongestSubstring(s)
