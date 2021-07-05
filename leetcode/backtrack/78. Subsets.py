# coding=utf-8

"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    def subsets(self, nums):
        """
        迭代法

        """

        results = [[]]

        for num in nums:
            l = []
            for result in results:
                l.append(result + [num])

            results.extend(l)
        return results


class Solution1:
    def subsets(self, nums):

        """
        2.顺序考虑，仅考虑选择的元素

        以空集[]开始，从第一个元素开始考虑，它有三种选择，1,2,3，组成[1]，[2]，[3]
        当第一个元素为1的时候，第二个元素可以选择的是1后面的元素2,3，组成[1,2]，[1,3]
        当第二个元素为2的时候，此时[1,2]，第三个元素可以选择3，组成[1,2,3]
        当第一个元素为2的时候，第二个元素可以选择3，组成[2,3]
        结束遍历，获得组成的8个答案，这说明了有效结果是没有条件的，任何结果都是有效的

        """

        self.res = []
        self.backtrack([], 0, nums)

        return self.res

    def backtrack(self, sol, index, nums):
        self.res.append(sol)

        for i in range(index, len(nums)):
            self.backtrack(sol + [nums[i]], i + 1, nums)


class Solution2(object):

    """
    1.全部考虑，选或不选

    1选或不选，有两种情况，2选或不选，有两种情况，3选或不选，有两种情况，那么总共就是2*2*2=8种情况：

    """
    def subsets(self, nums):
        self.res = []
        self.backtrack([], 0, nums)
        return self.res

    def backtrack(self, l, index, nums):

        # terminator
        if index == len(nums):
            self.res.append(l)
            return

        # pick the number at this index
        self.backtrack(l + [nums[index]], index + 1, nums)

        # not pick the number at this index
        self.backtrack(l, index + 1, nums)

        # reverse the current state


if __name__ == "__main__":
    print Solution().subsets([1,2,3])

