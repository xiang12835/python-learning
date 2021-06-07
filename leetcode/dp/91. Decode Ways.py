# coding=utf-8

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        1. subproblem

        2. dp array
        设 fi表示字符串 s 的前 i 个字符 s[1..i] 的解码方法数

        3. dp equation

        第一种情况是我们使用了一个字符，f(i) = f(i−1)，其中 s[i] != 0
        第二种情况是我们使用了两个字符，f(i) = f(i−2)，其中 s[i−1] != 0 并且 10⋅s[i−1]+s[i] ≤ 26

        or

        跟爬楼梯很类似，一次编码一个数字、或者一次编码两个数字。

        如果当前字符可以编码，但跟前一个字符无法编码，则：dp[i] = dp[i - 1]
        如果当前字符可以编码，且跟前一个字符也可以编码，则：dp[i] = dp[i - 1] + dp[i - 2]
        T: O(n)
        S: O(n)
        """
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # 空字符串可以有 1 种解码方法，解码出一个空字符串

        for i in range(1, n + 1):
            if s[i - 1] != '0':  # 如果当前字符不是0，则至少有一条转移路径，从dp[i-1]而来
                dp[i] = dp[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i - 2:i]) <= 26:  # 如果前一个+当前组合的数字，在有效范围内
                dp[i] += dp[i - 2]
        return dp[-1]