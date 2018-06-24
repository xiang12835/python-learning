# coding=utf-8


""" Queue（用于进程通信，资源共享）

在使用多进程的过程中，最好不要使用共享资源。普通的全局变量是不能被子进程所共享的，只有通过Multiprocessing组件构造的数据结构可以被共享。

Queue是用来创建进程间资源共享的队列的类，使用Queue可以达到多进程间数据传递的功能（缺点：只适用Process类，不能在Pool进程池中使用）。

构造方法：Queue([maxsize])

maxsize是队列中允许最大项数，省略则无大小限制。
实例方法：

put()：用以插入数据到队列。put方法还有两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，该方法会阻塞timeout指定的时间，直到该队列有剩余的空间。如果超时，会抛出Queue.Full异常。如果blocked为False，但该Queue已满，会立即抛出Queue.Full异常。
get()：可以从队列读取并且删除一个元素。get方法有两个可选参数：blocked和timeout。如果blocked为True（默认值），并且timeout为正值，那么在等待时间内没有取到任何元素，会抛出Queue.Empty异常。如果blocked为False，有两种情况存在，如果Queue有一个值可用，则立即返回该值，否则，如果队列为空，则立即抛出Queue.Empty异常。若不希望在empty的时候抛出异常，令blocked为True或者参数全部置空即可。
get_nowait()：同q.get(False)
put_nowait()：同q.put(False)
empty()：调用此方法时q为空则返回True，该结果不可靠，比如在返回True的过程中，如果队列中又加入了项目。
full()：调用此方法时q已满则返回True，该结果不可靠，比如在返回True的过程中，如果队列中的项目被取走。
qsize()：返回队列中目

"""

from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()  # 等待pw结束
pr.terminate()  # pr进程里是死循环，无法等待其结束，只能强行终止
