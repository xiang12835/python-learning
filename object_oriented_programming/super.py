# coding=utf-8


class AbstractShape:
    def __init__(self, color):
        self.color = color


class Circle(AbstractShape):
    def __init__(self, color, r=0.0):
        super().__init__(color)
        # AbstractShape.__init__(self, color)
        self.r = r

c = Circle("#FFFFFF")
