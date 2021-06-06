# coding=utf-8

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool

        https://leetcode-cn.com/problems/wildcard-matching/solution/liang-chong-shi-xian-xiang-xi-tu-jie-44-i7p61/

        视频讲解 https://leetcode-cn.com/problems/wildcard-matching/solution/dong-tai-gui-hua-dai-zhu-shi-by-tangweiqun/

        1. subproblem

        2. dp array

        dp[i][j]，表示S从开始到下标i，P从开始到下标j是否匹配

        3. dp equation

        T: O(m*n)
        S: O(m*n)
        """
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # S为空，P为空时两个字符串相等
        dp[0][0] = True
        # 当字符串S为空，模式串P不空，检查P中是否有*
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                # 如果P当前是 *
                # 此时 * 去匹配S的一个字符串，可以将S的当前字符去掉(dp[i-1][j])
                # 此时 * 去匹配空字符串，可以去掉P的当前字符(dp[i][j-1])
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

                # 否则，要看P和S的当前字符是否匹配，或者P当前字符为?
                # 如果当前字符匹配，从递归的角度看
                # 可以去掉S的当前字符，P的当前字符(dp[i-1][j-1])
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]