# coding=utf-8

# 创建上下文管理器
#
# 上下文管理器，通俗的介绍就是：在代码块执行前，先进行准备工作；在代码块执行完成后，做收尾的处理工作。
# with语句常伴随上下文管理器一起出现，经典场景有：

with open('test.txt', 'r') as file:
    for line in file.readlines():
        print(line)

# 通过with语句，代码完成了文件打开操作，并在调用结束，或者读取发生异常时自动关闭文件，即完成了文件读写之后的处理工作。
# 如果不通过上下文管理器的话，则会是这样的代码：

file = open('test.txt', 'r')
try:
    for line in file.readlines():
        print(line)
finally:
    file.close()

# 比较繁琐吧？所以说使用上下文管理器的好处就是，通过调用我们预先设置好的回调，自动帮我们处理代码块开始执行和执行完毕时的工作。
# 而通过自定义类的__enter__和__exit__方法，我们可以自定义一个上下文管理器。

class ReadFile(object):
    def __init__(self, filename):
        self.file = open(filename, 'r')

    def __enter__(self):
        return self.file

    def __exit__(self, type, value, traceback):
        # type, value, traceback 分别代表错误的类型、值、追踪栈
        self.file.close()
        # 返回 True 代表不抛出错误
        # 否则错误会被 with 语句抛出
        return True


# 然后可以以这样的方式进行调用：

with ReadFile('test.txt') as file_read:
    for line in file_read.readlines():
        print(line)

# 在调用的时候：
#
# with语句先暂存了ReadFile类的__exit__方法
# 然后调用ReadFile类的__enter__方法
# __enter__方法打开文件，并将结果返回给with语句
# 上一步的结果被传递给file_read参数
# 在with语句内对file_read参数进行操作，读取每一行
# 读取完成之后，with语句调用之前暂存的__exit__方法
# __exit__方法关闭了文件
# 要注意的是，在__exit__方法内，我们关闭了文件，但最后返回True，所以错误不会被with语句抛出。否则with语句会抛出一个对应的错误。
