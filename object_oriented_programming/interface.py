# coding=utf-8


# 用 python 实现一个接口

class AbstractShape:
    def area(self):
        raise NotImplementedError


a = AbstractShape()
try:
    a.area()
except NotImplementedError:
    pass



"""
你应该发现了，Entity 本身是没有什么用的，只需拿来定义 Document 和 Video 的一些基本元素就够了。不过，万一你不小心生成 Entity 的对象该怎么办呢？为了防止这样的手误，必须要介绍一下抽象类。

抽象类是一种特殊的类，它生下来就是作为父类存在的，一旦对象化就会报错。同样，抽象函数定义在抽象类之中，子类必须重写该函数才能使用。相应的抽象函数，则是使用装饰器 @abstractmethod 来表示。

我们可以看到，代码中 entity = Entity() 直接报错，只有通过 Document 继承 Entity  才能正常使用。

这其实正是软件工程中一个很重要的概念，定义接口。大型工程往往需要很多人合作开发，比如在 Facebook 中，在 idea 提出之后，开发组和产品组首先会召开产品设计会，PM（Product Manager，产品经理） 写出产品需求文档，然后迭代；TL（Team Leader，项目经理）编写开发文档，开发文档中会定义不同模块的大致功能和接口、每个模块之间如何协作、单元测试和集成测试、线上灰度测试、监测和日志等等一系列开发流程。

抽象类就是这么一种存在，它是一种自上而下的设计风范，你只需要用少量的代码描述清楚要做的事情，定义好接口，然后就可以交给不同开发人员去开发和对接。
"""


from abc import ABCMeta, abstractmethod


class Entity(metaclass=ABCMeta):
    @abstractmethod
    def get_title(self):
        pass

    @abstractmethod
    def set_title(self, title):
        pass


class Document(Entity):
    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title


document = Document()
document.set_title('Harry Potter')
print(document.get_title())

# entity = Entity()

