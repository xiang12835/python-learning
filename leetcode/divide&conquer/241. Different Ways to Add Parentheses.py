# coding=utf-8

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        """ 分治

        二叉树后序遍历

        该问题的子问题就是 x op y 中的 x 和 y：以运算符分隔的左右两侧算式解。

        """

        # 1. terminater: 如果只有数字，直接返回
        if expression.isdigit():
            return [int(expression)]

        res = []
        for i, ch in enumerate(expression):
            if ch in '+-*':
                # 2.divide：遇到运算符，计算左右两侧的结果集
                # 3.conquer：diffWaysToCompute 递归函数求出子问题的解
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                # 4.merge：根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        if ch == '+':
                            res.append(l + r)
                        elif ch == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)

        return res
