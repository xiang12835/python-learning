# coding=utf-8


'''默认情况下，dict迭代的是key'''
dic = {'a':1, 'b':2, 'c':3}

for key in dic:
    print(key)


'''如果要迭代value，可以用for value in d.values()'''
for value in dic.values():
    print value


'''如果要同时迭代key和value，可以用for k, v in d.items()'''
for k,v in dic.items():
    print k, v


'''字符串也是可迭代对象'''
for ch in 'ABC':
    print ch