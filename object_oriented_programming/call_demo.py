# coding=utf-8

# __call__
#
# 通过定义类中的__call__方法，可以使该类的实例能够像普通函数一样调用。


class AddNumber(object):
    def __init__(self):
        self.num = 0

    def __call__(self, num=1):
        self.num += num

add_number = AddNumber()
print(add_number.num)  # 0
add_number()  # 像方法一样的调用
print(add_number.num)  # 1
add_number(3)
print(add_number.num)  # 4

# 通过这种方式实现的好处是，可以通过类的属性来保存状态，而不必创建一个闭包或者全局变量。
