# coding=utf-8


x = [1,2,3]
y = [4,5,6]
z = [7,8,9]

xyz = zip(x,y,z)

print xyz


# 实例：构建字典序列
a = [1,2,3]
b = ['a','b','c']
lst = zip(a,b)
print lst

dic = dict(lst)
print dic



a = [1,2,3]
b = [4,5,6]
c = [4,5,6,7,8]
zipped = zip(a,b)     # 打包为元组的列表
print zipped
print zip(a,c)              # 元素个数与最短的列表一致
print zip(*zipped)          # 与 zip 相反，可理解为解压，返回二维矩阵式
