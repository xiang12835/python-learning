# coding=utf-8

"""

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool

        滑动窗口

        """

        if s == ''.join(wordDict):
            return True

        n = len(s)
        start = 0
        end = 1

        while end != n:
            if s[start:end] in wordDict:
                print end
                start = end
            else:
                end += 1

        print s[start:end]
        if s[start:end] in wordDict:
            return True

        return False


if __name__ == '__main__':
    s = "aaaaaaa"
    wordDict = ["aaaa", "aaa"]

    # s = "applepenapple"
    # wordDict = ["apple", "pen"]

    r = Solution().wordBreak(s, wordDict)
    print r
