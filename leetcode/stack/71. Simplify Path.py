# coding=utf-8

class Solution:
    def simplifyPath(self, path: str) -> str:
        """ 栈
        T: O(n)
        S: O(n)

        分类：. | .. | 字符
        """
        names = path.split('/')
        stack = []
        for name in names:
            if name == "..":
                if stack:
                    stack.pop()
            elif name and name != '.': # 字符
                stack.append(name)
        return '/' + '/'.join(stack)

