# -*- coding:utf-8 -*-


class Solution:
    # s 源字符串
    def replaceSpace1(self, s):
        # 法一：在Python中str类型是不可变的类型, 使用replace语句会生成一个新的str, 原始的s还是带空格的str变量
        if type(s) != str:
            return
        return s.replace(" ", "%20")

    def replaceSpace2(self, s):
        # 法二：创建新的字符串进行替换
        res = ''
        if type(s) != str:
            return
        for c in s:
            if c == ' ':
                res += '%20'
            else:
                res += c
        return res

    def replaceSpace3(self, s):
        # 法三：逆向思维
        # 如果直接每次遇到空格添加'%20'，那么空格后面的数字就需要频繁向后移动。
        # 遇到这种移动问题，我们可以尝试先给出最终需要的长度，然后从后向前扫描，同时给定两个指针来保证定位。
        pass

s = 'we are happy'
test = Solution()
print(test.replaceSpace1(s))
print(test.replaceSpace2(s))
