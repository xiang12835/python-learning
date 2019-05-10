# coding=utf-8

"""
单例模式（Singleton
Pattern）是一种常用的软件设计模式，该模式的主要目的是 ** 确保某一个类只有一个实例存在 **。当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。

在
Python
中，我们可以用多种方法来实现单例模式：

- 使用模块
- 使用__new__
- 使用装饰器（decorator）
- 使用元类（metaclass）

"""

# 1.使用__new__方法



class A(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


class B(A):
    a = 1




class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class MyClass(Singleton):
    a = 1



# 2.共享属性

# 创建实例时把所有实例的__dict__指向同一个字典, 这样它们具有相同的属性和方法.



class Borg(object):
    _state = {}

    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        ob.__dict__ = cls._state
        return ob


class MyClass2(Borg):
    a = 1



# 3.装饰器版本



def singleton(cls):
    instances = {}

    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return getinstance


@singleton
class MyClass:
    a = 1




"""4.import方法

# 作为python的模块是天然的单例模式

# mysingleton.py
class My_Singleton(object):
    def foo(self):
        pass


my_singleton = My_Singleton()

# to use
from mysingleton import my_singleton

my_singleton.foo()
"""



"""单例模式的应用场景有哪些?


比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。如果在程序运行期间，有很多地方都需要使用配置文件的内容，也就是说，很多地方都需要创建 AppConfig 对象的实例，这就导致系统中存在多个 AppConfig 的实例对象，而这样会严重浪费内存资源，尤其是在配置文件内容很多的情况下。事实上，类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象。

单例模式应用的场景一般发现在以下条件:

(1)资源共享的情况下，避免由于资源操作时导致的性能或损耗等。如日志文件，应用配置。

(2)控制资源的情况下，方便资源之间的互相通信。如线程池等。

- 网站的计数器
- 应用配置
- 多线程池
- 数据库配置，数据库连接池
- 应用程序的日志应用

"""