# coding=utf-8

from typing import List


class Solution(object):
    def permute(self, nums):

        """回溯

        https://pic.leetcode-cn.com/0bf18f9b86a2542d1f6aa8db6cc45475fce5aa329a07ca02a9357c2ead81eec1-image.png

        递归的终止条件是： 一个排列中的数字已经选够了 ，因此我们需要一个变量来表示当前程序递归到第几层，我们把这个变量叫做 depth，或者命名为 index ，表示当前要确定的是某个全排列中下标为 index 的那个数是多少；

        path 变量是一个栈

        对象类型变量在传参的过程中，复制的是变量的地址。这些地址被添加到 res 变量，但实际上指向的是同一块内存地址，因此我们会看到 6 个空的列表对象。解决的方法很简单，在 res.add(path); 这里做一次拷贝即可。

        布尔数组 used，初始化的时候都为 false 表示这些数还没有被选择，当我们选定一个数的时候，就将这个数组的相应位置设置为 true ，这样在考虑下一个位置的时候，就能够以 O(1)O(1) 的时间复杂度判断这个数是否被选择过，这是一种「以空间换时间」的思想。

        T: O(n×n!)
        S: O(n×n!)

        """
        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        self.backtrack(nums, size, 0, [], used, res)
        return res

    def backtrack(self, nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    print("  before => ", path)
                    self.backtrack(nums, size, depth + 1, path, used, res)

                    used[i] = False
                    path.pop()
                    print("after => ", path)



if __name__ == '__main__':
    nums = [1, 2]
    solution = Solution()
    res = solution.permute(nums)
    print(res)

