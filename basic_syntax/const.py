# coding=utf-8

""" 将常量集中到一个文件

Python 的内建命名空间是支持一小部分常量的，例如 True、False、None 等，只是 Python 没有提供定义常量的直接方式而已。

在 Python 中应该如何使用常量？一般来说有以下两种方式：
1) 通过命名风格来提醒使用者该变量代表的意义为常量，如常量名所有字母大写，用下划线连接各个单词
2) 通过自定义的类实现常量功能。这要求符合”命名全部为大写“和”值一旦绑定便不可再修改“这两个条件。下面是一种较为常见的解决办法，它通过对常量对应的值进行修改时或者命名不符合规范时抛出异常来满足以上常量的两个条件。

class _const:
    class ConstError(TypeError):
        pass
    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "Can't change const.{}".format(name)
        if not name.isupper():
            raise self.ConstCaseError, "const name {} is not all uppercase".format(name)
        self.__dict__[name] = value

import sys
sys.modules[__name__] = _const()

如果上面的代码对应的模块名为 const，使用时候只需要 import const，便可以直接定义常量了，如以下代码：

import const
const.COMPANY = "IBM"

无论采用哪一种方式来实现常量，都提倡将常量集中到一个文件中，因为这样有利于维护，一旦需要修改常量的值，可以集中统一而不是逐个文件去检查。采用第二种方式实现的常量可以这么做：将存放常量的文件命名为 constant.py ，并在其中定义一系列的常量。

class _const:
    [...]

import sys
sys.modules[__name__] = _const()
import const
const.MY_CONSTANT = 1
const.MY_SECOND_CONSTANT = 2

当在其他模块中引用这些常量时，按照如下方式进行即可：

from constant import const
print(const.MY_SECOND_CONSTANT)

"""
