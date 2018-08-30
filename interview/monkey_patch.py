# coding=utf-8

# 什么是猴子补丁？

class Foo(object):
    def bar(self):
        print('Foo.bar')

def bar(self):
    print('Modified bar')

Foo().bar()

Foo.bar = bar  # 在运行期间动态修改一个类或模块。

Foo().bar()
