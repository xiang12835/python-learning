# coding=utf-8

""" Multiprocessing产生的背景


除了应对Python的GIL以外，产生multiprocessing的另外一个原因时Windows操作系统与Linux/Unix系统的不一致。

Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（父进程）复制了一份（子进程），然后，分别在父进程和子进程内返回。

子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getpid()就可以拿到父进程的ID。

有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。


"""

import os
print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:  #子进程
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:  #父进程
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))





"""  Python的多进程包multiprocessing



Python的threading包主要运用多线程的开发，但由于GIL的存在，Python中的多线程其实并不是真正的多线程，如果想要充分地使用多核CPU的资源，大部分情况需要使用多进程。在Python 2.6版本的时候引入了multiprocessing包，它完整的复制了一套threading所提供的接口方便迁移。唯一的不同就是它使用了多进程而不是多线程。每个进程有自己的独立的GIL，因此也不会出现进程之间的GIL争抢。

借助这个multiprocessing，你可以轻松完成从单进程到并发执行的转换。multiprocessing支持子进程、通信和共享数据、执行不同形式的同步，提供了Process、Queue、Pipe、Lock等组件。



multiprocessing常用组件及功能
创建管理进程模块：

Process（用于创建进程）
Pool（用于创建管理进程池）
Queue（用于进程通信，资源共享）
Value，Array（用于进程通信，资源共享）
Pipe（用于管道通信）
Manager（用于资源共享）
同步子进程模块：

Condition（条件变量）
Event（事件）
Lock（互斥锁）
RLock（可重入的互斥锁(同一个进程可以多次获得它，同时不会造成阻塞)
Semaphore（信号量）

"""
