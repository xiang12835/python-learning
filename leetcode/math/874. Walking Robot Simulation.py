# coding=utf-8

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        di, x, y = 0, 0, 0
        distance = 0
        obs_dict = {}
        for obs in obstacles:
            obs_dict[tuple(obs)] = 0
        for com in commands:
            if com == -2: # 向左转 90 度
                di = (di + 3)%4
            elif com == -1: # 向右转 90 度
                di = (di + 1)%4
            else:
                for j in range(com):
                    next_x = x + dx[di]
                    next_y = y + dy[di]
                    if (next_x, next_y) in obs_dict: # 遇到障碍物
                        break
                    x, y = next_x, next_y
                    distance = max(distance, x*x + y*y)
        return distance


class Solution1:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        """
        S：O(N+K)，其中 N,K 分别是 commands 和 obstacles 的长度。
        T：O(K)，用于存储 obstacleSet 而使用的空间。
        """

        # 方向
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        di = 0

        x = y = 0

        distance = 0

        obstacles_set = set()
        for obs in obstacles:
            obstacles_set.add(tuple(obs))

        for com in commands:
            if com == -2: # 左转
                di = (di + 3) % 4
            elif com == -1: # 右转
                di = (di + 1) % 4
            else: # 一步一步走，判断是否前方有障碍
                for _ in range(com):
                    cur_x = x + dx[di]
                    cur_y = y + dy[di]

                    if (cur_x, cur_y) in obstacles_set: # 遇到障碍物，停留
                        break

                    x, y = cur_x, cur_y # 易错
                    distance = max(distance, x*x + y*y)

        return distance