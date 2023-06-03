from datetime import datetime


class Person:

    def __init__(self, name, age):
        """Конструктор, принимающий имя и возраст человека"""
        self.name = name
        self.age = age

    def display(self):
        """ Метод, выводящий на экран имя и возраст человека """
        print(f'{self.name} is {self.age} years old')

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """
        Класс-метод, принимающий имя и год рождения человека и
        возвращающий объект класса Person
        """
        now = datetime.now()
        age = now.year - int(birth_year)
        return cls(name, age)

    @staticmethod
    def is_adult(age):
        """
        Статический метод, принимающий возраст человека и возвращающий True,
        если он старше 18 лет, и False в противном случае
        """
        if age >= 18:
            return True
        return False


person1 = Person("John", 28)
person1.display()  # John is 28 years old

person2 = Person.from_birth_year("Mike", 1995)
person2.display()  # Mike is 28 years old in 2023

print(Person.is_adult(20))  # True
print(Person.is_adult(15))  # False
