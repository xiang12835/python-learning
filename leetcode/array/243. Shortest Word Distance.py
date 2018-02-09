"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = "coding", word2 = "practice", return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        idx1 = idx2 = -1
        r = len(words)
        for i in xrange(len(words)):
            if words[i] == word1:
                idx1 = i
            elif words[i] == word2:
                idx2 = i
            if idx1 != -1 and idx2 != -1:
                r = min(r, abs(idx2 - idx1))

        return r


if __name__ == "__main__":
    s = Solution()
    words = ["practice", "makes", "perfect", "coding", "makes"]

    word1 = "coding"
    word2 = "practice"

    word3 = "makes"
    word4 = "coding"

    print s.shortestDistance(words, word1, word2)
    print s.shortestDistance(words, word3, word4)
