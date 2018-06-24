# coding=utf-8


'''

Semaphore（信号量）
信号量是一个更高级的锁机制。信号量内部有一个计数器而不像锁对象内部有锁标识，而且只有当占用信号量的线程数超过信号量时线程才阻塞。这允许了多个线程可以同时访问相同的代码区。比如厕所有3个坑，那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去，如果指定信号量为3，那么来一个人获得一把锁，计数加1，当计数等于3时，后面的人均需要等待。一旦释放，就有人可以获得一把锁。

构造方法：Semaphore([value])

value：设定信号量，默认值为1
实例方法：

acquire([timeout])：同Lock
release(): 同Lock
使用示例：


'''


from multiprocessing import Process, Semaphore
import time, random


def go_wc(sem, user):
    sem.acquire()
    print('%s used' % user)
    time.sleep(random.randint(0, 3))
    sem.release()
    print(user, 'OK')


if __name__ == '__main__':
    sem = Semaphore(2)
    p_l = []
    for i in range(5):
        p = Process(target=go_wc, args=(sem, 'user%s' % i,))
        p.start()
        p_l.append(p)
    for i in p_l:
        i.join()
