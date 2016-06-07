# coding=utf-8
'''
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
'''


# 比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现
def f(x):
    return x*x

r = map(f, [1, 2, 3, 4, 5])
print list(r) # 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。


# 把这个list所有数字转为字符串
print list(map(str, [1,2,3,4,5]))


# 练习: 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
# capitalize() 首字母大写，其余全部小写
# upper() 全转换成大写
# lower() 全转换成小写
# title()  标题首字大写，如"i love python".title()  "I love python"

def normalize(name):
    return name.capitalize()

def normalize1(name):
    return name[0].upper() + name[1:].lower()

print map(normalize, ['baiDu', 'aliBAba', 'TenCent'])
print map(normalize1, ['baiDu', 'aliBAba', 'TenCent'])
