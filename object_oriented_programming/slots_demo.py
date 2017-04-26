# coding=utf-8

# __slots__
#
# 默认情况下，Python 用一个字典来保存一个对象的实例属性。这使得我们可以在运行的时候动态的给类的实例添加新的属性：
#
# test = Test()
# test.new_key = 'new_value'
# 然而这个字典浪费了多余的空间 --- 很多时候我们不会创建那么多的属性。因此通过__slots__可以告诉 Python 不要使用字典而是固定集合来分配空间。


class Test(object):
    # 用列表罗列所有的属性
    __slots__ = ['name', 'value']

    def __init__(self, name='test', value='0'):
        self.name = name
        self.value = value

test = Test()
# 此时再增加新的属性则会报错
test.new_key = 'new_value'
# AttributeError: 'Test' object has no attribute 'new_key'
