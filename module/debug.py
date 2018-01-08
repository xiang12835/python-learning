# coding=utf-8


# 1 pirnt()
# def foo(s):
#     n = int(s)
#     print('>>> n = %d' % n)
#     return 10 / n
#
# def main():
#     foo('0')
#
# main()
# 用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。


# 2 assert
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
# def main():
#     foo('0')
# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert


# 3 logging
# import logging
# logging.basicConfig(level=logging.INFO)
#
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)


# 4 pdb
# s = '0'
# n = int(s)
# print(10 / n)
# 命令: l n p q


import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
# 命令: p c

# 5 IDE - pycharm
