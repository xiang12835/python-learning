from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/bao-li-jie-fa-zhan-by-liweiwei1419/

        时间复杂度：O(N)，输入数组里的每一个元素入栈一次，出栈一次。
        空间复杂度：O(N)，栈的空间最多为 N。

        """
        size = len(heights)
        res = 0
        heights = [0] + heights + [0]
        # 先放入哨兵结点，在循环中就不用做非空判断
        stack = [0]
        size += 2

        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                res = max(res, cur_height * cur_width)
            stack.append(i)
        return res


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]

    solution = Solution()
    res = solution.largestRectangleArea(heights)
    print(res)

