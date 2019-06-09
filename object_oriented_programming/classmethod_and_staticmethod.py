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


########## 类函数 & 成员函数 & 静态函数 ##########

# 如何在一个类中定义一些常量，每个对象都可以方便访问这些常量而不用重新构造？
# 如果一个函数不涉及到访问修改这个类的属性，而放到类外面有点不恰当，怎么做才能更优雅呢？
# 既然类是一群相似的对象的集合，那么可不可以是一群相似的类的集合呢？

class Document():
    WELCOME_STR = 'Welcome! The context for this book is {}.'  # 第一个问题，在 Python 的类里，你只需要和函数并列地声明并赋值，就可以实现这一点，例如这段代码中的 WELCOME_STR。一种很常规的做法，是用全大写来表示常量，因此我们可以在类中使用 self.WELCOME_STR ，或者在类外使用 Entity.WELCOME_STR ，来表达这个字符串。

    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context

    # 类函数
    @classmethod
    def create_empty_book(cls, title, author):
        # 而类函数的第一个参数一般为 cls，表示必须传一个类进来。类函数最常用的功能是实现不同的 init 构造函数，比如上文代码中，我们使用 create_empty_book 类函数，来创造新的书籍对象，其 context 一定为'nothing'。
        return cls(title=title, author=author, context='nothing')

    # 成员函数
    def get_context_length(self):
        # 成员函数则是我们最正常的类的函数，它不需要任何装饰器声明，第一个参数 self 代表当前对象的引用，可以通过此函数，来实现想要的查询 / 修改类的属性等功能。
        return len(self.__context)

    # 静态函数
    @staticmethod
    def get_welcome(context):
        # 一般而言，静态函数可以用来做一些简单独立的任务，既方便测试，也能优化代码结构。静态函数还可以通过在函数前一行加上 @staticmethod 来表示，代码中也有相应的示例。
        return Document.WELCOME_STR.format(context)


empty_book = Document.create_empty_book('What Every Man Thinks About Apart from Sex', 'Professor Sheridan Simove')

print(empty_book.get_context_length())
print(empty_book.get_welcome('indeed nothing'))



