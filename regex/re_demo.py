# coding=utf-8

import re


def test_search():
    data = "abcdakdjd"
    pattern = r"a.*?d"  # 懒惰匹配：尽量匹配最短串
    # pattern = r"a.*d"  # 贪婪匹配：要匹配最长串
    match = re.search(pattern, data, re.S)
    r = match.group(0) if match else ""
    return r


if __name__ == "__main__":
    print test_search()

