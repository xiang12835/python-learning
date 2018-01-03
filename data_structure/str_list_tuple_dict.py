# coding=utf-8

mytuple = (1, 2, 3)  # Tuple to list
print list(mytuple)

mylist = [1, 2, 3]  # List to tuple
print tuple(mylist)

mylist2 = [('blue', 5), ('red', 3), ('yellow', 7)]  # List to dictionary
print dict(mylist2)

mystring = 'hello'  # String to list
print list(mystring)

mylist3 = ['w', 'or', 'ld']  # List to string
print ''.join(mylist3)
