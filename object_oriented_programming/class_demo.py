# coding=utf-8


class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def set(self, x, y):  # self 并不是关键字，甚至可以用其它名字替代，比如 this
        self.x, self.y = x, y


p = Point(10, 10)  # __init__ 被调用

# Point 是 type 的一个实例，这和 p 是 Point 的一个实例是一回事Point 是 type 的一个实例，这和 p 是 Point 的一个实例是一回事
print type(p)
print type(Point)


print dir(Point)  # ['__doc__', '__init__', '__module__', 'set']
print Point.__module__


# p.set(...) 其实只是一个语法糖，你也可以写成 Point.set(p, ...)，这样就能明显看出 p 就是 self 参数了：
print p.x, p.y
p.set(0, 0)
print p.x, p.y
Point.set(p, 1, 1)
print p.x, p.y



########## 类 ##########


class Document():
    def __init__(self, title, author, context):  # 构造函数，意即一个对象生成时会被自动调用的函数
        print('init function called')
        self.title = title  # 属性
        self.author = author  # 属性
        self.__context = context  # __ 开头的属性是私有属性。私有属性，是指不希望在类的函数之外的地方被访问和修改的属性

    def get_context_length(self):  # 类的普通函数，我们调用它来对对象的属性做一些事情
        return len(self.__context)

    def intercept_context(self, length):  # 类的普通函数，我们调用它来对对象的属性做一些事情
        self.__context = self.__context[:length]

harry_potter_book = Document('Harry Potter', 'J. K. Rowling', '... Forever Do not believe any thing is capable of thinking independently ...')

print(harry_potter_book.title)
print(harry_potter_book.author)
print(harry_potter_book.get_context_length())

harry_potter_book.intercept_context(10)

print(harry_potter_book.get_context_length())

# print(harry_potter_book.__context)




