"""
Напишите класс Animal, представляющий животное, имеющий следующие методы:

- __init__(self, name): конструктор, принимающий имя животного;
- speak(self): метод, который выводит звук, издаваемый животным.

Напишите класс Dog, наследующийся от класса Animal, представляющий собаку, имеющий следующие методы:

- speak(self): метод, который выводит звук, издаваемый собакой.

Напишите класс Cat, наследующийся от класса Animal, представляющий кошку, имеющий следующие методы:

- speak(self): метод, который выводит звук, издаваемый кошкой.
"""


class Animal:
    def __init__(self, name):
        """Конструктор, принимающий имя животного"""
        self.name = name

    def speak(self):
        """Метод, который выводит звук, издаваемый животным"""
        return 'Звук животного'


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        """Метод, который выводит звук, издаваемый собакой"""
        return 'Woof!'


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        """Метод, который выводит звук, издаваемый кошкой"""
        return 'Meow!'


if __name__ == '__main__':

    animal = Animal("Animal")
    print(animal.speak())  # ?

    dog = Dog("Dog")
    print(dog.speak())  # Woof!

    cat = Cat("Cat")
    print(cat.speak())  # Meow!
