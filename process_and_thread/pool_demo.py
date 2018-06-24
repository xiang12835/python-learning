# coding=utf-8


""" Pool（用于创建管理进程池）

Pool类用于需要执行的目标很多，而手动限制进程数量又太繁琐时，如果目标少且不用控制进程数量则可以用Process类。
Pool可以提供指定数量的进程，供用户调用，当有新的请求提交到Pool中时，如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到规定最大值，那么该请求就会等待，直到池中有进程结束，就重用进程池中的进程。

构造方法：Pool([processes[, initializer[, initargs[, maxtasksperchild[, context]]]]])

processes ：要创建的进程数，如果省略，将默认使用cpu_count()返回的数量。
initializer：每个工作进程启动时要执行的可调用对象，默认为None。如果initializer是None，那么每一个工作进程在开始的时候会调用initializer(*initargs)。
initargs：是要传给initializer的参数组。
maxtasksperchild：工作进程退出之前可以完成的任务数，完成后用一个新的工作进程来替代原进程，来让闲置的资源被释放。maxtasksperchild默认是None，意味着只要Pool存在工作进程就会一直存活。
context: 用在制定工作进程启动时的上下文，一般使用Pool() 或者一个context对象的Pool()方法来创建一个池，两种方法都适当的设置了context。
实例方法：

apply(func[, args[, kwargs]])：在一个池工作进程中执行func(args,*kwargs),然后返回结果。需要强调的是：此操作并不会在所有池工作进程中并执行func函数。如果要通过不同参数并发地执行func函数，必须从不同线程调用p.apply()函数或者使用p.apply_async()。它是阻塞的。apply很少使用
apply_async(func[, arg[, kwds={}[, callback=None]]])：在一个池工作进程中执行func(args,*kwargs),然后返回结果。此方法的结果是AsyncResult类的实例，callback是可调用对象，接收输入参数。当func的结果变为可用时，将理解传递给callback。callback禁止执行任何阻塞操作，否则将接收其他异步操作中的结果。它是非阻塞。
map(func, iterable[, chunksize=None])：Pool类中的map方法，与内置的map函数用法行为基本一致，它会使进程阻塞直到返回结果。 注意，虽然第二个参数是一个迭代器，但在实际使用中，必须在整个队列都就绪后，程序才会运行子进程。
map_async(func, iterable[, chunksize=None])：map_async与map的关系同apply与apply_async
imap()：imap 与 map的区别是，map是当所有的进程都已经执行完了，并将结果返回了，imap()则是立即返回一个iterable可迭代对象。
imap_unordered()：不保证返回的结果顺序与进程添加的顺序一致。
close()：关闭进程池，防止进一步操作。如果所有操作持续挂起，它们将在工作进程终止前完成。
join()：等待所有工作进程退出。此方法只能在close()或teminate()之后调用，让其不再接受新的Process。
terminate()：结束工作进程，不再处理未处理的任务。
方法apply_async()和map_async()的返回值是AsyncResul的实例obj。实例具有以下方法：

get()：返回结果，如果有必要则等待结果到达。timeout是可选的。如果在指定时间内还没有到达，将引发异常。如果远程操作中引发了异常，它将在调用此方法时再次被引发。
ready()：如果调用完成，返回True
successful()：如果调用完成且没有引发异常，返回True，如果在结果就绪之前调用此方法，引发异常
wait([timeout])：等待结果变为可用。
terminate()：立即终止所有工作进程，同时不执行任何清理或结束任何挂起工作。如果p被垃圾回收，将自动调用此函数

"""


# Pool+map
from multiprocessing import Pool


def test(i):
    print(i)


if __name__ == "__main__":
    lists = range(100)
    pool = Pool(8)
    pool.map(test, lists)
    pool.close()
pool.join()


'''  异步进程池（非阻塞）

from multiprocessing import Pool


def test(i):
    print(i)


if __name__ == "__main__":
    pool = Pool(8)
    for i in range(100):
        '''
        For循环中执行步骤：
        （1）循环遍历，将100个子进程添加到进程池（相对父进程会阻塞）
        （2）每次执行8个子进程，等一个子进程执行完后，立马启动新的子进程。（相对父进程不阻塞）
        apply_async为异步进程池写法。异步指的是启动子进程的过程，与父进程本身的执行（print）是异步的，而For循环中往进程池添加子进程的过程，与父进程本身的执行却是同步的。
        '''
        pool.apply_async(test, args=(i,))  # 维持执行的进程总数为8，当一个进程执行完后启动一个新进程.
    print("test")
    pool.close()
    pool.join()
'''

''' 异步进程池（非阻塞）

from multiprocessing import Pool

def test(i):
    print(i)

if __name__ == "__main__":
    pool = Pool(8)
    for i in range(100):
        '''
            实际测试发现，for循环内部执行步骤：
            （1）遍历100个可迭代对象，往进程池放一个子进程
            （2）执行这个子进程，等子进程执行完毕，再往进程池放一个子进程，再执行。（同时只执行一个子进程）
            for循环执行完毕，再执行print函数。
        '''
        pool.apply(test, args=(i,))  # 维持执行的进程总数为8，当一个进程执行完后启动一个新进程.
    print("test")
    pool.close()
    pool.join()

'''
