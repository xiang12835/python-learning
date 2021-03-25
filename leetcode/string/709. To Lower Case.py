# coding=utf-8

class Solution:
    def toLowerCase(self, str: str) -> str:
        """
        return str.lower()

        'A' - 'Z' 对应的 ascii 是 65 - 90；
		'a' - 'z' 对应的 ascii 是 97 - 122；
		大小字母转换相差32，解题只要记住ord(),chr()函数即可
        """

        l = []
        for c in str:
            if 65 <= ord(c) <= 90:
                l.append(chr(ord(c) + 32))
            else:
                l.append(c)
        return "".join(l)
