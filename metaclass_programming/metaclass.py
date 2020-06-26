# coding=utf-8

'''

python3

动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。

metaclass，直译为元类，先定义metaclass，就可以创建类，最后创建实例。

ORM就是一个典型的例子。虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。

metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为。这种强大的功能使用起来务必小心。

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

class MyList(list, metaclass=ListMetaclass):  #  元类可以创建类
    pass

l = MyList() # 通过创建的类来创建实例
l.add(1)

print(l)
