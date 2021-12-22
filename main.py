class Rectangle:
    all_rectangles = []

    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB
        self.area_ = self.area(sideA, sideB)
        self.__class__.all_rectangles.append(self)

    def area(self):
        return self.sideA*self.sideB

    @staticmethod
    def area_any(side_1, side_2):
        return side_1*side_2

    @classmethod
    def area_all(cls):
        areas = []
        i = 0
        for shape in cls:
            areas[i] = shape.area()
            i += 1
        return areas


class Square(Rectangle):
    def __init__(self, side):
        super(Square, self).__init__(side, side)


