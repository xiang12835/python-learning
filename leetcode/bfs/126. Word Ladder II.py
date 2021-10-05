# coding=utf-8

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        BFS
        """

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        queue = [(beginWord, [beginWord])]
        visited = {beginWord}

        ans = []
        while queue:

            cur_size = len(queue)

            for _ in range(cur_size):

                word, path = queue.pop(0)

                if word == endWord:
                    ans.append(path)

                n = len(word)
                for i in range(n):
                    for j in range(26):
                        next_word = word[:i] + chr(ord("a") + j) + word[i + 1:]

                        if next_word in wordSet:
                            queue.append((next_word, path + [next_word]))

                            if next_word not in visited:
                                visited.add(next_word)

            wordSet -= visited  # 去重

        return ans


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    print(Solution().findLadders(beginWord, endWord, wordList))



