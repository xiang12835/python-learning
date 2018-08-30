# coding=utf-8

'''
另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
意义:因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
'''

t1 = (1)
print t1

t2 = (1,) # 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
print t2

# 来看一个“可变的”tuple
t3 = ('a', 'b', ['A', 'B'])
t3[2][0] = 'x'
t3[2][1] = 'y'
print t3
# 解释:tuple所谓的“不变”是说，tuple的每个元素，指向永远不变,指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！



# 元组的解封装是什么？
mytuple=3,4,5
print mytuple

x,y,z=mytuple
print x+y+z
