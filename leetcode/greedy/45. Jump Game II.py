# coding=utf-8

class Solution:
    def jump(self, nums):
        """
        Greedy

        T: O(N)
        S: O(1)

        """
        size = len(nums)
        max_dis = 0
        end = 0
        step = 0
        for i in range(size - 1):
            if i <= max_dis:
                max_dis = max(max_dis, i + nums[i])  # 找能跳的最远的
                if i == end:  # 遇到边界，就更新边界，并且步数加一
                    end = max_dis
                    step += 1
        return step

if __name__ == "__main__":
    s = Solution()
    print(s.jump([2,3,1,1,4]))
