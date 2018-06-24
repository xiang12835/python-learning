# coding=utf-8


"""
Manager（用于资源共享）
Manager()返回的manager对象控制了一个server进程，此进程包含的python对象可以被其他的进程通过proxies来访问。从而达到多进程间数据通信且安全。Manager模块常与Pool模块一起使用。

Manager支持的类型有list,dict,Namespace,Lock,RLock,Semaphore,BoundedSemaphore,Condition,Event,Queue,Value和Array。

管理器是独立运行的子进程，其中存在真实的对象，并以服务器的形式运行，其他进程通过使用代理访问共享对象，这些代理作为客户端运行。Manager()是BaseManager的子类，返回一个启动的SyncManager()实例，可用于创建共享对象并返回访问这些共享对象的代理。

BaseManager，创建管理器服务器的基类

构造方法：BaseManager([address[, authkey]])

address：(hostname,port),指定服务器的网址地址，默认为简单分配一个空闲的端口
authkey：连接到服务器的客户端的身份验证，默认为current_process().authkey的值
实例方法：

start([initializer[, initargs]])：启动一个单独的子进程，并在该子进程中启动管理器服务器
get_server()：获取服务器对象
connect()：连接管理器对象
shutdown()：关闭管理器对象，只能在调用了start()方法之后调用
实例属性：

address：只读属性，管理器服务器正在使用的地址
SyncManager，以下类型均不是进程安全的，需要加锁..

实例方法：

Array(self,*args,**kwds)
BoundedSemaphore(self,*args,**kwds)
Condition(self,*args,**kwds)
Event(self,*args,**kwds)
JoinableQueue(self,*args,**kwds)
Lock(self,*args,**kwds)
Namespace(self,*args,**kwds)
Pool(self,*args,**kwds)
Queue(self,*args,**kwds)
RLock(self,*args,**kwds)
Semaphore(self,*args,**kwds)
Value(self,*args,**kwds)
dict(self,*args,**kwds)
list(self,*args,**kwds)

"""


import multiprocessing


def f(x, arr, l, d, n):
    x.value = 3.14
    arr[0] = 5
    l.append('Hello')
    d[1] = 2
    n.a = 10


if __name__ == '__main__':
    server = multiprocessing.Manager()
    x = server.Value('d', 0.0)
    arr = server.Array('i', range(10))
    l = server.list()
    d = server.dict()
    n = server.Namespace()

    proc = multiprocessing.Process(target=f, args=(x, arr, l, d, n))
    proc.start()
    proc.join()

    print(x.value)
    print(arr)
    print(l)
    print(d)
    print(n)
