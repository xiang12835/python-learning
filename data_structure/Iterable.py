# coding=utf-8


# 凡是可作用于for循环的对象都是Iterable类型


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


# 迭代
''' 1
需要获取 index 时使用enumerate
enumerate可以接受第二个参数，作为迭代时加在index上的数值
'''
list = ['a', 'b', 'c', 'd']

for index, value in enumerate(list):
    print(index)
# 0
# 1
# 2
# 3

for index, value in enumerate(list, 2):
    print(index)
# 2
# 3
# 4
# 5

''' 2
用zip同时遍历两个迭代器
'''
list_a = ['a', 'b', 'c', 'd']
list_b = [1, 2, 3]
# 虽然列表长度不一样，但只要有一个列表耗尽，则迭代就会停止
for letter, number in zip(list_a, list_b):
    print(letter, number)
# a 1
# b 2
# c 3

''' 3
zip遍历时返回一个元组
'''
a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']
for i in zip(a,b):
    print(i)

# (1, 'w')
# (2, 'x')
# (3, 'y')

''' 4
关于for和while循环后的else块
循环正常结束之后会调用else内的代码
循环里通过break跳出循环，则不会执行else
要遍历的序列为空时，立即执行else
'''
for i in range(2):
    print(i)
else:
    print('loop finish')
# 0
# 1
# loop finish

for i in range(2):
    print(i)
    if i % 2 == 0:
        break
else:
    print('loop finish')
# 0

for i in []:
    print(i)
else:
    print('loop finish')
# loop finish
