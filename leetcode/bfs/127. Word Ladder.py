# coding=utf-8

import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int

        广度优先搜索 + 建图

        T：O(N * C^2)。其中 N 为 wordList 的长度，C 为列表中单词的平均长度。
        S：O(N * C^2)。其中 N 为 wordList 的长度，C 为列表中单词的平均长度。

        法二：DFS

        法三：Two-ended BFS

        """
        # 先将 wordList 放到哈希表里，便于判断某个单词是否在 wordList 里
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0

        if beginWord in word_set:
            word_set.remove(beginWord)
        # 双端队列，图的广度优先遍历，必须使用队列和表示是否访问过的 visited 哈希表
        queue = collections.deque()
        queue.append(beginWord)
        visited = set(beginWord)

        word_len = len(beginWord)

        # 开始广度优先遍历，包含起点，因此初始化的时候步数为 1
        step = 1
        while queue:
            current_size = len(queue)

            # 依次遍历当前队列中的单词
            for _ in range(current_size):
                word = queue.popleft()
                word_list = list(word)
                # 如果 currentWord 能够修改 1 个字符与 endWord 相同，则返回 step + 1
                for j in range(word_len):
                    # 先保存，然后恢复
                    origin_char = word_list[j]
                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visited:
                                queue.append(next_word)
                                # 添加到队列以后，必须马上标记为已经访问
                                visited.add(next_word)
                    # 恢复
                    word_list[j] = origin_char
            step += 1
        return 0




class Solution1:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        双向BFS
        """
        set_list = set(wordList)
        if not wordList or endWord not in set_list:
            return 0
        visited = {beginWord, endWord}
        left, right = {beginWord}, {endWord}
        number = 0
        length = len(beginWord)
        # 当前层中数量少的给left,多的给right
        while left:
            number += 1
            next_level = set()
            for word in left:
                for j in range(length):
                    for m in range(26):
                        new_word = word[:j] + chr(ord('a') + m) + word[j + 1:]
                        if new_word in right:
                            return number + 1
                        if new_word not in visited and new_word in set_list:
                            visited.add(new_word)
                            next_level.add(new_word)
            left = next_level
            # 加入下面两行代码就实现了双向BFS：
            if len(left) > len(right):
                left, right = right, left
        return 0


class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        广度优先搜索 + 建图

        T：O(N * C^2)。其中 N 为 wordList 的长度，C 为列表中单词的平均长度。
        S：O(N * C^2)。其中 N 为 wordList 的长度，C 为列表中单词的平均长度。

        法二：DFS

        法三：Two-ended BFS
        """

        # 先将 wordList 放到哈希表里，便于判断某个单词是否在 wordList 里
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0

        if beginWord in word_set:
            word_set.remove(beginWord)

        # 队列，图的广度优先遍历，必须使用队列和表示是否访问过的 visited 哈希表
        queue = [(beginWord, 1)]
        visited = set(beginWord)

        word_len = len(beginWord)

        # 开始广度优先遍历，包含起点，因此初始化的时候步数为 1
        while queue:

            cur_size = len(queue)
            for _ in range(cur_size):

                word, step = queue.pop(0)
                if word == endWord:
                    return step
                # 如果 currentWord 能够修改 1 个字符与 endWord 相同，则返回 step + 1
                for j in range(word_len):
                    for k in range(26):
                        next_word = word[:j] + chr(ord('a') + k) + word[j+1:]
                        if next_word in word_set and next_word not in visited:
                            queue.append((next_word, step+1))
                            # 添加到队列以后，必须马上标记为已经访问
                            visited.add(next_word)
        return 0


