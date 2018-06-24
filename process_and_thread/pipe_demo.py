# coding=utf-8

"""
Pipe（用于管道通信）
多进程还有一种数据传递方式叫管道原理和 Queue相同。Pipe可以在进程之间创建一条管道，并返回元组（conn1,conn2）,其中conn1，conn2表示管道两端的连接对象，强调一点：必须在产生Process对象之前产生管道。

构造方法：Pipe([duplex])

dumplex:默认管道是全双工的，如果将duplex射成False，conn1只能用于接收，conn2只能用于发送。
实例方法：

send(obj)：通过连接发送对象。obj是与序列化兼容的任意对象
recv()：接收conn2.send(obj)发送的对象。如果没有消息可接收，recv方法会一直阻塞。如果连接的另外一端已经关闭，那么recv方法会抛出EOFError。
close():关闭连接。如果conn1被垃圾回收，将自动调用此方法
fileno():返回连接使用的整数文件描述符
poll([timeout]):如果连接上的数据可用，返回True。timeout指定等待的最长时限。如果省略此参数，方法将立即返回结果。如果将timeout射成None，操作将无限期地等待数据到达。
recv_bytes([maxlength]):接收c.send_bytes()方法发送的一条完整的字节消息。maxlength指定要接收的最大字节数。如果进入的消息，超过了这个最大值，将引发IOError异常，并且在连接上无法进行进一步读取。如果连接的另外一端已经关闭，再也不存在任何数据，将引发EOFError异常。
send_bytes(buffer [, offset [, size]])：通过连接发送字节数据缓冲区，buffer是支持缓冲区接口的任意对象，offset是缓冲区中的字节偏移量，而size是要发送字节数。结果数据以单条消息的形式发出，然后调用c.recv_bytes()函数进行接收
recv_bytes_into(buffer [, offset]):接收一条完整的字节消息，并把它保存在buffer对象中，该对象支持可写入的缓冲区接口（即bytearray对象或类似的对象）。offset指定缓冲区中放置消息处的字节位移。返回值是收到的字节数。如果消息长度大于可用的缓冲区空间，将引发BufferTooShort异常。
使用示例：

"""

from multiprocessing import Process, Pipe
import time


#子进程执行方法
def f(Subconn):
    time.sleep(1)
    Subconn.send("have you eat")
    print("father say:", Subconn.recv())
    Subconn.close()


if __name__ == "__main__":
    parent_conn, child_conn = Pipe()  #创建管道两端
    p = Process(target=f, args=(child_conn,))  #创建子进程
    p.start()
    print("son say:", parent_conn.recv())
    parent_conn.send("yes")
