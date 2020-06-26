# coding=utf-8

'''

python3

动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
metaclass，直译为元类，先定义metaclass，就可以创建类，最后创建实例。
'''

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

h = Hello()
h.hello()
print(type(Hello)) # type()函数可以查看一个类型或变量的类型
print(type(h))


# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

l = MyList()
l.add(1)
