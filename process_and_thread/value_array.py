# coding=utf-8

"""
alue，Array（用于进程通信，资源共享）
multiprocessing 中Value和Array的实现原理都是在共享内存中创建ctypes()对象来达到共享数据的目的，两者实现方法大同小异，只是选用不同的ctypes数据类型而已。

Value

构造方法：Value((typecode_or_type, args[, lock])

typecode_or_type：定义ctypes()对象的类型，可以传Type code或 C Type，具体对照表见下文。
args：传递给typecode_or_type构造函数的参数
lock：默认为True，创建一个互斥锁来限制对Value对象的访问，如果传入一个锁，如Lock或RLock的实例，将用于同步。如果传入False，Value的实例就不会被锁保护，它将不是进程安全的。
typecode_or_type支持的类型：

| Type code | C Type             | Python Type       | Minimum size in bytes |
| --------- | ------------------ | ----------------- | --------------------- |
| `'b'`     | signed char        | int               | 1                     |
| `'B'`     | unsigned char      | int               | 1                     |
| `'u'`     | Py_UNICODE         | Unicode character | 2                     |
| `'h'`     | signed short       | int               | 2                     |
| `'H'`     | unsigned short     | int               | 2                     |
| `'i'`     | signed int         | int               | 2                     |
| `'I'`     | unsigned int       | int               | 2                     |
| `'l'`     | signed long        | int               | 4                     |
| `'L'`     | unsigned long      | int               | 4                     |
| `'q'`     | signed long long   | int               | 8                     |
| `'Q'`     | unsigned long long | int               | 8                     |
| `'f'`     | float              | float             | 4                     |
| `'d'`     | double             | float             | 8                     |
参考地址：docs.python.org/3/library/a…

Array

构造方法：Array(typecode_or_type, size_or_initializer, **kwds[, lock])

typecode_or_type：同上
size_or_initializer：如果它是一个整数，那么它确定数组的长度，并且数组将被初始化为零。否则，size_or_initializer是用于初始化数组的序列，其长度决定数组的长度。
kwds：传递给typecode_or_type构造函数的参数
lock：同上


注意：Value和Array只适用于Process类。

"""


import multiprocessing

def f(n, a):
    n.value = 3.14
    a[0] = 5

if __name__ == '__main__':
    num = multiprocessing.Value('d', 0.0)
    arr = multiprocessing.Array('i', range(10))
    p = multiprocessing.Process(target=f, args=(num, arr))
    p.start()
    p.join()
    print(num.value)
    print(arr[:])
