# coding=utf-8

class Solution:
    def decodeString(self, s: str) -> str:
        """
        T: O(n)
        S: O(n)
        """
        stack = []
        res = ""
        multi = 0
        for c in s:
            if c == '[':  # 入栈
                stack.append((multi, res))
                res = ""
                multi = 0
            elif c == ']':  # 出栈
                cur_multi, cur_res = stack.pop()
                res = cur_res + cur_multi * res
            elif '0' <= c <= '9':  # 数字 -- 倍数
                multi = multi * 10 + int(c)
            else:  # 字母
                res += c

        return res
