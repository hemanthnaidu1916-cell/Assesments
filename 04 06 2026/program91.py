class Shape:
    def area(self):
        print(0)   # Default area


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length * self.length)


s1 = Shape()
s1.area()

s2 = Square(5)
s2.area()
