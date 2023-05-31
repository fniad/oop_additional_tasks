"""
Напишите класс Shape, представляющий геометрическую фигуру, имеющей следующие методы:

- __init__(self, name): конструктор, принимающий имя геометрической фигуры;
- area(self): метод, который вычисляет площадь геометрической фигуры.

Напишите класс Rectangle, наследующийся от класса Shape, представляющий прямоугольник, имеющий следующие методы:

- __init__(self, name, width, height): конструктор, принимающий имя прямоугольника, ширину и высоту;
- area(self): метод, который вычисляет площадь прямоугольника.

Напишите класс Triangle, наследующийся от класса Shape, представляющий треугольник, имеющий следующие методы:

- __init__(self, name, base, height): конструктор, принимающий имя треугольника, основание и высоту;
- area(self): метод, который вычисляет площадь треугольника.
"""


class Shape:
    def __init__(self, name):
        """Конструктор, принимающий имя геометрической фигуры"""
        self.name = name

    def area(self):
        """Метод, который вычисляет площадь геометрической фигуры"""
        return 0


class Rectangle(Shape):
    def __init__(self, name, width, height):
        """Конструктор, принимающий имя прямоугольника, ширину и высоту"""
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        """Метод, который вычисляет площадь прямоугольника"""
        return self.height * self.width


class Triangle(Shape):
    def __init__(self, name, base, height):
        """Конструктор, принимающий имя треугольника, основание и высоту"""
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        """Метод, который вычисляет площадь треугольника"""
        return (self.base * self.height) // 2


if __name__ == '__main__':
    shape = Shape("Shape")
    print(shape.area())  # 0

    rect = Rectangle("Rectangle", 5, 10)
    print(rect.area())  # 50

    tri = Triangle("Triangle", 6, 4)
    print(tri.area())  # 12
