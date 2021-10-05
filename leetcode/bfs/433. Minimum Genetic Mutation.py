# coding=utf-8

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        # 广度优先搜索
        bank = set(bank)  # 转换为set, in判断只需O(1)时间
        if end not in bank:  # 目标不可行，直接返回-1
            return -1
        queue = [(start, 0)]  # 初始结点以及当前步数
        change = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}  # 每个基因对应的可变换基因
        while queue:  # 用队列实现广度优先
            node, step = queue.pop(0)
            if node == end:  # 已经到达目标
                return step
            for i, v in enumerate(node):  # 当前序列的每一个基因
                for j in change[v]:  # 该基因可以改变的方式
                    new = node[:i]+j+node[i+1:]  # 改变后的序列
                    if new in bank:  # 如果该序列可行
                        queue.append((new, step+1))  # 入队，继续广度搜索
                        bank.remove(new)  # 避免重复遍历
        return -1  # 队列空了说明不可达


class Solution1:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
        双向BFS
        """
        if end not in bank:
            return -1
        start_set = {start}
        end_set = {end}
        bank = set(bank)
        length = 0
        change_map = {'A': 'TCG', 'T': 'ACG', 'C': 'ATG', 'G': 'ATC'}
        while start_set:
            length += 1
            new_set = set()
            for node in start_set:
                for i, s in enumerate(node):
                    for c in change_map[s]:
                        new = node[:i] + c + node[i + 1:]
                        if new in end_set:
                            return length
                        if new in bank:
                            new_set.add(new)
                            bank.remove(new)
            start_set = new_set
            if len(end_set) < len(start_set):
                start_set, end_set = end_set, start_set
        return -1


class Solution2:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
        BFS
        """

        if end not in bank:
            return -1

        queue = [(start, 0)] # 初始结点以及当前步数
        change = ["A", "C", "G", "T"]
        while queue: # 用队列实现广度优先

            cur_size = len(queue)
            for _ in range(cur_size):

                node, step = queue.pop(0)
                if node == end: # 已经到达目标
                    return step

                for i in range(len(node)):
                    for c in change:
                        new = node[:i] + c + node[i + 1:] # 改变后的序列
                        if new in bank:
                            queue.append((new, step + 1)) # 入队，继续广度搜索
                            bank.remove(new) # 避免重复遍历

        return -1