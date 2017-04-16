#!/usr/bin/python2
# coding=utf-8

# 题目：4个数中有一个数不同，两次找到不同的数
test1 = [1, 2, 2, 2]
test2 = [2, 1, 2, 2]
test3 = [2, 2, 1, 2]
test4 = [2, 2, 2, 1]
test5 = [4, 4, 4, 4, 4, 6, 4, 4, 4]
test6 = [1, 2, 3]
test7 = [1, 2]
test8 = [1, 1, 1]


# 两次的
def find_diff_num(l=[]):
    if l[0] != l[1] and l[0] != l[2]:
        res = l[0]
    elif l[0] != l[1] and l[0] == l[2]:
        res = l[1]
    elif l[0] == l[1] and l[0] != l[2]:
        res = l[2]
    elif l[0] == l[1] and l[0] == l[2]:
        res = l[3]
    return res

print find_diff_num(test1)
print find_diff_num(test2)
print find_diff_num(test3)
print find_diff_num(test4)


# 考虑扩展性
def get_diff_num_for_common(l=[]):
    if len(l) < 3 or len(set(l)) != 2:
        return "cannot find the diff num!"
    elif l[0] != l[1] and l[1] == l[2]:
        res = l[0]
    elif l[-1] != l[-2] and l[-2] == l[-3]:
        res = l[-1]
    else:
        for i in range(len(l)-2):
            if l[i] != l[i+1] and l[i+1] != l[i+2]:
                res = l[i+1]
    return res

print get_diff_num_for_common(test1)
print get_diff_num_for_common(test2)
print get_diff_num_for_common(test3)
print get_diff_num_for_common(test4)
print get_diff_num_for_common(test5)
print get_diff_num_for_common(test6)
print get_diff_num_for_common(test7)
print get_diff_num_for_common(test8)
