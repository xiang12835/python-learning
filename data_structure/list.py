# coding=utf-8

classmates = ['Michael', 'Bob', 'Tracy']
print classmates

print len(classmates)

print classmates[1]

print classmates[-1]

classmates.append('Adam') # 往list中追加元素到末尾
print classmates

classmates.insert(1, 'Jack') # 可以把元素插入到指定的位置
print classmates

classmates.pop() # 要删除list末尾的元素
print classmates

classmates.pop(1) # 要删除指定位置的元素
print classmates

classmates[1] = 'Sarah' # 要把某个元素替换成别的元素
print classmates

L = ['Apple', 123, True] # list里面的元素的数据类型也可以不同
print L

s = ['python', 'java', ['asp', 'php'], 'scheme'] # list元素也可以是另一个list
print len(s)

L = []
print len(L)


# 列表切割
#
# list[start:end:step]
# 如果从列表开头开始切割，那么忽略 start 位的 0，例如list[:4]
# 如果一直切到列表尾部，则忽略 end 位的 0，例如list[3:]
# 切割列表时，即便 start 或者 end 索引跨界也不会有问题
# 列表切片不会改变原列表。索引都留空时，会生成一份原列表的拷贝
a = [1, 2, 3]
b = a[:]
assert b == a and b is not a  # true