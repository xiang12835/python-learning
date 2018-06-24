# coding=utf-8

"""
Lock（互斥锁）
Lock锁的作用是当多个进程需要访问共享资源的时候，避免访问的冲突。加锁保证了多个进程修改同一块数据时，同一时间只能有一个修改，即串行的修改，牺牲了速度但保证了数据安全。Lock包含两种状态——锁定和非锁定，以及两个基本的方法。

构造方法： Lock()

实例方法：

acquire([timeout]): 使线程进入同步阻塞状态，尝试获得锁定。
release(): 释放锁。使用前线程必须已获得锁定，否则将抛出异常。
使用示例：


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
