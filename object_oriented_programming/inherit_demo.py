# coding=utf-8
import math


class Shape:
    def area(self):
        return 0.0


class Circle(Shape):
    def __init__(self, r=0.0):
        self.r = r

    # def area(self):
    #     return math.pi * self.r * self.r

Circle.area = lambda self: math.pi * self.r * self.r  # 子类重写父类的方法，其实只是把相同的属性名绑定到了不同的函数对象。


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def area(self):
        return self.a * self.b

circle = Circle(3.0)
print circle.area()

rectangle = Rectangle(2.0, 3.0)
print rectangle.area()


""" 继承

首先需要注意的是构造函数。每个类都有**构造函数**，继承类在生成对象的时候，是不会自动调用父类的构造函数的，因此你必须在 init() 函数中显式调用父类的构造函数。它们的执行顺序是 子类的构造函数 -> 父类的构造函数。

其次需要注意父类 get_context_length() 函数。如果使用 Entity 直接生成对象，调用 get_context_length() 函数，就会 raise error 中断程序的执行。这其实是一种很好的写法，叫做**函数重写**，可以使子类必须重新写一遍 get_context_length() 函数，来覆盖掉原有函数。

最后需要注意到 print_title() 函数，这个函数定义在父类中，但是子类的对象可以毫无阻力地使用它来打印 title，这也就体现了继承的优势：**减少重复的代码，降低系统的熵值（即复杂度）**。

"""


class Entity():
    def __init__(self, object_type):
        print('parent class init called')
        self.object_type = object_type

    def get_context_length(self):
        raise Exception('get_context_length not implemented')

    def print_title(self):
        print(self.title)


class Document(Entity):
    def __init__(self, title, author, context):
        print('Document class init called')
        Entity.__init__(self, 'document')
        self.title = title
        self.author = author
        self.__context = context

    def get_context_length(self):
        return len(self.__context)


class Video(Entity):
    def __init__(self, title, author, video_length):
        print('Video class init called')
        Entity.__init__(self, 'video')
        self.title = title
        self.author = author
        self.__video_length = video_length

    def get_context_length(self):
        return self.__video_length


harry_potter_book = Document('Harry Potter(Book)', 'J. K. Rowling',
                             '... Forever Do not believe any thing is capable of thinking independently ...')
harry_potter_movie = Video('Harry Potter(Movie)', 'J. K. Rowling', 120)

print(harry_potter_book.object_type)
print(harry_potter_movie.object_type)

harry_potter_book.print_title()
harry_potter_movie.print_title()

print(harry_potter_book.get_context_length())
print(harry_potter_movie.get_context_length())




