# coding=utf-8


# one example
class Point:
    def __init__(self, x=0, y=0):
        self.__x, self.__y = x, y

    def set(self, x, y):
        self.__x, self.__y = x, y

    def __f(self):
        pass

p = Point(10, 10)
try:
    p.__x   # __x、__y 和 __f 就相当于私有了
except Exception as e:
    print e

print p._Point__x


# another example
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'c'

bart = Student('Bart Simpson', 59)
print('bart.get_name() = ', bart.get_name())

bart.set_score(60)
print('bart.get_score() =', bart.get_score())

print('DO NOT use bart._Student__name:', bart._Student__name)
