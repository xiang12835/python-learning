# coding=utf-8


"""
Process（用于创建进程）
multiprocessing模块提供了一个Process类来代表一个进程对象。

在multiprocessing中，每一个进程都用一个Process类来表示。

构造方法：Process([group [, target [, name [, args [, kwargs]]]]])

group：分组，实际上不使用，值始终为None
target：表示调用对象，即子进程要执行的任务，你可以传入方法名
name：为子进程设定名称
args：要传给target函数的位置参数，以元组方式进行传入。
kwargs：要传给target函数的字典参数，以字典方式进行传入。
实例方法：

start()：启动进程，并调用该子进程中的p.run()
run()：进程启动时运行的方法，正是它去调用target指定的函数，我们自定义类的类中一定要实现该方法
terminate()：强制终止进程p，不会进行任何清理操作，如果p创建了子进程，该子进程就成了僵尸进程，使用该方法需要特别小心这种情况。如果p还保存了一个锁那么也将不会被释放，进而导致死锁
is_alive()：返回进程是否在运行。如果p仍然运行，返回True
join([timeout])：进程同步，主进程等待子进程完成后再执行后面的代码。线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）。timeout是可选的超时时间（超过这个时间，父线程不再等待子线程，继续往下执行），需要强调的是，p.join只能join住start开启的进程，而不能join住run开启的进程
属性介绍：

daemon：默认值为False，如果设为True，代表p为后台运行的守护进程；当p的父进程终止时，p也随之终止，并且设定为True后，p不能创建自己的新进程；必须在p.start()之前设置
name：进程的名称
pid：进程的pid
exitcode：进程在运行时为None、如果为–N，表示被信号N结束(了解即可)
authkey：进程的身份验证键,默认是由os.urandom()随机生成的32字符的字符串。这个键的用途是为涉及网络连接的底层进程间通信提供安全性，这类连接只有在具有相同的身份验证键时才能成功（了解即可）
使用示例：（注意：在windows中Process()必须放到if __name__ == ‘__main__’:下）
"""


from multiprocessing import Process
import os


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
