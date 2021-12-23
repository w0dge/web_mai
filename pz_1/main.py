class Rectangle:
    all_rectangles = []

    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB
        self.__class__.all_rectangles.append(self)

    def area(self):
        return self.sideA * self.sideB

    @staticmethod
    def area_any(side_1, side_2):
        return side_1 * side_2

    @classmethod
    def area_all(cls):
        areas = []
        for shape in cls.all_rectangles:
            areas.append(shape.area())
        return areas


class Square(Rectangle):
    def __init__(self, side):
        super(Square, self).__init__(side, side)


rect = Rectangle(3, 5)
square = Square(3)

print(rect.area())
print(square.area())
print(rect.area_all())
