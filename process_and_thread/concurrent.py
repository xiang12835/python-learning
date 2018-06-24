# coding=utf-8

"""  concurrent

Python并发之concurrent.futures
Python标准库为我们提供了threading和multiprocessing模块编写相应的多线程/多进程代码。从Python3.2开始，标准库为我们提供了concurrent.futures模块，它提供了ThreadPoolExecutor和ProcessPoolExecutor两个类，实现了对threading和multiprocessing的更高级的抽象，对编写线程池/进程池提供了直接的支持。 concurrent.futures基础模块是executor和future。

Executor
Executor是一个抽象类，它不能被直接使用。它为具体的异步执行定义了一些基本的方法。 ThreadPoolExecutor和ProcessPoolExecutor继承了Executor，分别被用来创建线程池和进程池的代码。

ThreadPoolExecutor对象
ThreadPoolExecutor类是Executor子类，使用线程池执行异步调用。

class concurrent.futures.ThreadPoolExecutor(max_workers)
使用max_workers数目的线程池执行异步调用。

ProcessPoolExecutor对象
ThreadPoolExecutor类是Executor子类，使用进程池执行异步调用.

class concurrent.futures.ProcessPoolExecutor(max_workers=None)
使用max_workers数目的进程池执行异步调用，如果max_workers为None则使用机器的处理器数目（如4核机器max_worker配置为None时，则使用4个进程进行异步并发）。

submit()方法
Executor中定义了submit()方法，这个方法的作用是提交一个可执行的回调task，并返回一个future实例。future对象代表的就是给定的调用。

Executor.submit(fn, *args, **kwargs)

fn：需要异步执行的函数
*args, **kwargs：fn参数
使用示例：

from concurrent import futures

def test(num):
    import time
    return time.ctime(), num

with futures.ThreadPoolExecutor(max_workers=1) as executor:
    future = executor.submit(test, 1)
    print(future.result())


"""

"""  map()方法

除了submit，Exectuor还为我们提供了map方法，这个方法返回一个map(func, *iterables)迭代器，迭代器中的回调执行返回的结果有序的。

Executor.map(func, *iterables, timeout=None)

func：需要异步执行的函数
*iterables：可迭代对象，如列表等。每一次func执行，都会从iterables中取参数。
timeout：设置每次异步操作的超时时间，timeout的值可以是int或float，如果操作超时，会返回raisesTimeoutError；如果不指定timeout参数，则不设置超时间。
使用示例：

from concurrent import futures

def test(num):
    import time
    return time.ctime(), num

data = [1, 2, 3]
with futures.ThreadPoolExecutor(max_workers=1) as executor:
    for future in executor.map(test, data):
        print(future)



"""

""" shutdown()


shutdown()方法
释放系统资源,在Executor.submit()或 Executor.map()等异步操作后调用。使用with语句可以避免显式调用此方法。

Executor.shutdown(wait=True)

Future
Future可以理解为一个在未来完成的操作，这是异步编程的基础。通常情况下，我们执行io操作，访问url时（如下）在等待结果返回之前会产生阻塞，cpu不能做其他事情，而Future的引入帮助我们在等待的这段时间可以完成其他的操作。

Future类封装了可调用的异步执行。Future 实例通过 Executor.submit()方法创建。

cancel()：试图取消调用。如果调用当前正在执行，并且不能被取消，那么该方法将返回False，否则调用将被取消，方法将返回True。
cancelled()：如果成功取消调用，返回True。
running()：如果调用当前正在执行并且不能被取消，返回True。
done()：如果调用成功地取消或结束了，返回True。
result(timeout=None)：返回调用返回的值。如果调用还没有完成，那么这个方法将等待超时秒。如果调用在超时秒内没有完成，那么就会有一个Futures.TimeoutError将报出。timeout可以是一个整形或者浮点型数值，如果timeout不指定或者为None,等待时间无限。如果futures在完成之前被取消了，那么 CancelledError 将会报出。
exception(timeout=None)：返回调用抛出的异常，如果调用还未完成，该方法会等待timeout指定的时长，如果该时长后调用还未完成，就会报出超时错误futures.TimeoutError。timeout可以是一个整形或者浮点型数值，如果timeout不指定或者为None,等待时间无限。如果futures在完成之前被取消了，那么 CancelledError 将会报出。如果调用完成并且无异常报出，返回None.
add_done_callback(fn)：将可调用fn捆绑到future上，当Future被取消或者结束运行，fn作为future的唯一参数将会被调用。如果future已经运行完成或者取消，fn将会被立即调用。
wait(fs, timeout=None, return_when=ALL_COMPLETED)
等待fs提供的 Future 实例(possibly created by different Executor instances) 运行结束。返回一个命名的2元集合，分表代表已完成的和未完成的
return_when 表明什么时候函数应该返回。它的值必须是一下值之一：
FIRST_COMPLETED :函数在任何future结束或者取消的时候返回。
FIRST_EXCEPTION ：函数在任何future因为异常结束的时候返回，如果没有future报错，效果等于
ALL_COMPLETED :函数在所有future结束后才会返回。
as_completed(fs, timeout=None)： 参数是一个 Future 实例列表，返回值是一个迭代器，在运行结束后产出 Future实例 。
使用示例：

from concurrent.futures import ThreadPoolExecutor, wait, as_completed
from time import sleep
from random import randint


def return_after_5_secs(num):
    sleep(randint(1, 5))
    return "Return of {}".format(num)


pool = ThreadPoolExecutor(5)
futures = []
for x in range(5):
    futures.append(pool.submit(return_after_5_secs, x))
print(1)
for x in as_completed(futures):
    print(x.result())
print(2)
参考链接：

pythonhosted.org/futures/
www.rddoc.com/doc/Python/…
hellowac.github.io/programing%…

"""
