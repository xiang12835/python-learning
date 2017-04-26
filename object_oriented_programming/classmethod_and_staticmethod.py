# coding=utf-8

'''
@classmethod和@staticmethod很像，但他们的使用场景并不一样。

1) 类内部普通的方法，都是以self作为第一个参数，代表着通过实例调用时，将实例的作用域传入方法内；
2) @classmethod以cls作为第一个参数，代表将类本身的作用域传入。无论通过类来调用，还是通过类的实例调用，默认传入的第一个参数都将是类本身
3) @staticmethod不需要传入默认参数，类似于一个普通的函数
'''


# 来通过实例了解它们的使用场景：
#
# 假设我们需要创建一个名为Date的类，用于储存 年/月/日 三个数据
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


# 好处：
#
# 在@classmethod内，可以通过cls参数，获取到跟外部调用类时一样的便利
# 可以在其中进一步封装该方法，提高复用性
# 更加符合面向对象的编程方式


''' 关于staticmethod
而@staticmethod，因为其本身类似于普通的函数，所以可以把和这个类相关的 helper 方法作为@staticmethod，放在类里，然后直接通过类来调用这个方法。
在 Date2 内新增一个 staticmethod
'''


class Date2(object):
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

    @staticmethod
    def is_month_validate(month):
        return int(month) <= 12 and int(month) >= 1
# 将与日期相关的辅助类函数作为@staticmethod方法放在Date类内后，可以通过类来调用这些方法：

month = '13'
if not Date2.is_month_validate(month):
    print '{} is a invalidate month number'.format(month)
