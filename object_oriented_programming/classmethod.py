# coding=utf-8


class Date(object):
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    @property
    def time(self):
        return "{year}-{month}-{day}".format(
            year=self.year,
            month=self.month,
            day=self.day
        )


date = Date('2016', '11', '09')
print date.time  # 2016-11-09


''' 改进1
但如果我们想改变属性传入的方式呢？毕竟，在初始化时就要传入年/月/日三个属性还是很烦人的。
能否找到一个方法，在不改变现有接口和方法的情况下，可以通过传入2016-11-09这样的字符串来创建一个Date实例？
'''

date_string = '2016-11-09'
year, month, day = map(str, date_string.split('-'))
date = Date(year, month, day)
print date.time


''' 改进2
但不够好：

1）在类外额外多写了一个方法，每次还得格式化以后获取参数
2）这个方法也只跟Date类有关
3）没有解决传入参数过多的问题

此时就可以利用@classmethod，在类的内部新建一个格式化字符串，并返回类的实例的方法：
'''


class Date1(object):
    def __init__(self, year=0, month=0, day=0):
        self.year = year
        self.month = month
        self.day = day

    @property
    def time(self):
        return "{year}-{month}-{day}".format(
            year=self.year,
            month=self.month,
            day=self.day
        )

    # 在 Date 内新增一个 classmethod
    @classmethod
    def from_string(cls, string):
        year, month, day = map(str, string.split('-'))
        # 在 classmethod 内可以通过 cls 来调用到类的方法，甚至创建实例
        date = cls(year, month, day)
        return date

date = Date1.from_string('2016-11-09')
print date.time

# 旧的实例化方式仍可以使用
date_old = Date1('2016', '11', '09')
print date_old.time
