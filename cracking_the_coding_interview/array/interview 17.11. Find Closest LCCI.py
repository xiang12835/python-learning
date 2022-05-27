# coding=utf-8

class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        """ 遍历

        一次遍历，记录单词的下标，同时计算最小下标差

        T: O(N)
        S: O(1)
        """
        index1 = -1
        index2 = -1
        ans = len(words)

        for i, v in enumerate(words):
            if v == word1:
                index1 = i
            if v == word2:
                index2 = i
            if index1 != -1 and index2 != -1:
                ans = min(ans, abs(index1-index2))

        return ans
