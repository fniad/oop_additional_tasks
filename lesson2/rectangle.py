class Rectangle:

    def __init__(self, width: float, height: float):
        """Конструктор, принимающий ширину и высоту прямоугольника"""
        self.width = width
        self.height = height

    def area(self):
        """Метод, возвращающий площадь прямоугольника"""
        return self.width * self.height

    def perimeter(self):
        """Метод, возвращающий периметр прямоугольника"""
        return (self.width + self.height) * 2

    @classmethod
    def from_diagonal(cls, diagonal):
        """Класс-метод, принимающий диагональ прямоугольника и возвращающий объект класса Rectangle"""
        width = round((diagonal / (2 ** 0.5)), 1)
        height = round((diagonal / (2 ** 0.5)), 1)
        return cls(width, height)

    @staticmethod
    def is_square(width, height):
        """
        Статический метод, принимающий ширину
        и высоту прямоугольника и возвращающий True,
        если это квадрат, и False в противном случае
        """
        if width == height:
            return True
        return False


rectangle = Rectangle(4, 5)
print(rectangle.area())  # 20
print(rectangle.perimeter())  # 18

rectangle2 = Rectangle.from_diagonal(5)
print(rectangle2.area())  # 12.5
print(rectangle2.perimeter())  # 10 ??

print(Rectangle.is_square(4, 4))  # True
print(Rectangle.is_square(4, 5))  # False
