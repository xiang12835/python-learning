# coding=utf-8


"""题目描述

输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。

输入描述:

输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。


"""


class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []

        res = []
        self.recursion(ss, res, '')
        return sorted(set(res))

    def recursion(self, ss, res, path):
        if ss == '':
            res.append(path)
        else:
            for i in xrange(len(ss)):
                self.recursion(ss[:i] + ss[i + 1:], res, path + ss[i])


class Solution1:
    def permutation(self, s):
        """
         回溯

        path 变量是一个栈，对象类型变量在传参的过程中，复制的是变量的地址。这些地址被添加到 res 变量，但实际上指向的是同一块内存地址，因此我们会看到 6 个空的列表对象。解决的方法很简单，在 res.add(path); 这里做一次拷贝即可。

        布尔数组 used，初始化的时候都为 false 表示这些数还没有被选择，当我们选定一个数的时候，就将这个数组的相应位置设置为 true ，这样在考虑下一个位置的时候，就能够以 O(1) 的时间复杂度判断这个数是否被选择过，这是一种「以空间换时间」的思想。

        T: O(n×n!)
        S: O(n×n!)
        """
        size = len(s)
        if size == 0:
            return ""

        ss = list(s)
        used = [False for _ in range(size)] # 布尔数组
        self.res = []
        self.backtrack(ss, size, 0, [], used)
        return self.res

    def backtrack(self, ss, size, depth, path, used):
        if depth == size:
            data = "".join(path)
            if data not in self.res:
                self.res.append(data)
                return

        for i in range(size):
            if not used[i]:
                used[i] = True
                path.append(ss[i])

                self.backtrack(ss, size, depth + 1, path, used)

                used[i] = False
                path.pop()


if __name__ == '__main__':
    ss = 'ab'
    Solution().Permutation(ss)
