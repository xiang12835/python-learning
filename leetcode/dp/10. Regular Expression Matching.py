# coding=utf-8


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        #S和P都为空时，匹配
        dp[0][0] = True
        #当S为空，P不空，要看P是否为 a*b*这种结构
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                #当前字符串是*，可以将 字符+*全部忽略掉，取f[i][j-2]的值
                #或者看模式串P的上一个字符串是否能跟字符串S匹配
                #如果能匹配上，可以忽略掉模式串的 字符+*，也可以忽略掉字符串S中的当前字符
                #这里其实跟递归一样，也有两条转移路径
                if p[j - 1] == "*":
                    if p[j - 2] in (s[i - 1], "."):
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]
                #单个字符匹配的情况
                else:
                    if p[j - 1] in (s[i - 1], "."):
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[-1][-1]
