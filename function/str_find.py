# coding=utf-8


info = 'abca'
print info.find('a')    # 从下标0开始，查找在字符串里第一个出现的子串，返回结果：0

print info.find('a', 1)  # 从下标1开始，查找在字符串里第一个出现的子串：返回结果3

print info.find('3')    # 查找不到返回-1
