# coding=utf-8


# interview1
def extend_list(val, lst=[]):
    lst.append(val)
    return lst

list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3

''' cause
因为带有默认参数的表达式在函数被定义的时候被计算，不是在调用的时候被计算。因此list1和list3是在同一个默认列表上进行操作（计算）的。
而list2是在一个分离的列表上进行操作（计算）的。（通过传递一个自有的空列表作为列表参数的数值）。
'''


# modify
def extend_list_new(val, lst=None):
    if lst is None:
        lst = []
    lst.append(val)
    return lst

list4 = extend_list_new(10)
list5 = extend_list_new(123, [])
list6 = extend_list_new('a')


print ">>>>>>>>> modify"
print "list4 = %s" % list4
print "list5 = %s" % list5
print "list6 = %s" % list6


# interview2
# 2,4,6,8行将输出什么结果？试解释。
list_a = [[]] * 5
print list_a  # output?
list_a[0].append(10)   # list[0].append(10) 将10附加在第一个列表上。但由于所有5个列表是引用的同一个列表
print list_a  # output?
list_a[1].append(20)
print list_a  # output?
list_a.append(30)
print list_a  # output?
