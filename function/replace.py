# coding=utf-8

# str是不变对象，而list是可变对象


'''对于可变对象，比如list，对list进行操作，list内部的内容是会变化的'''
a = ['a', 'c', 'b']
a.sort()
print a



'''而对于不可变对象，比如str，对str进行操作'''
a = 'abc'
b = a.replace('a', 'A')
print a
print b
