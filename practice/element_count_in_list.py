# coding=utf-8


def func(l=[]):
    res = {}
    new_l = list(set(l))
    for i in new_l:
        count = 0
        for j in l:
            if j == i:
                count += 1
        res[i] = count
    return res


l = ["2", "2", "3", "4", "2", "3", "5", "1"]
res = func(l)
print res
