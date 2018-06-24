# coding=utf-8

"""
Lock（互斥锁）
Lock锁的作用是当多个进程需要访问共享资源的时候，避免访问的冲突。加锁保证了多个进程修改同一块数据时，同一时间只能有一个修改，即串行的修改，牺牲了速度但保证了数据安全。Lock包含两种状态——锁定和非锁定，以及两个基本的方法。

构造方法： Lock()

实例方法：

acquire([timeout]): 使线程进入同步阻塞状态，尝试获得锁定。
release(): 释放锁。使用前线程必须已获得锁定，否则将抛出异常。

======================

RLock（可重入的互斥锁(同一个进程可以多次获得它，同时不会造成阻塞)
RLock（可重入锁）是一个可以被同一个线程请求多次的同步指令。RLock使用了“拥有的线程”和“递归等级”的概念，处于锁定状态时，RLock被某个线程拥有。拥有RLock的线程可以再次调用acquire()，释放锁时需要调用release()相同次数。可以认为RLock包含一个锁定池和一个初始值为0的计数器，每次成功调用 acquire()/release()，计数器将+1/-1，为0时锁处于未锁定状态。

构造方法：RLock()

实例方法：

acquire([timeout])：同Lock
release(): 同Lock


"""


from multiprocessing import Process, Lock


def l(lock, num):
    lock.acquire()
    print("Hello Num: %s" % (num))
    lock.release()


if __name__ == '__main__':
    lock = Lock()  #这个一定要定义为全局
    for num in range(20):
        Process(target=l, args=(lock, num)).start()
