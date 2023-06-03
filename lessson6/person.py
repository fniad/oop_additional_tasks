"""
Напишите класс Person, представляющий человека, имеющий следующие атрибуты:

- __slots__ = ('name', 'age'): список атрибутов, доступных объекту.

Напишите класс Employee, наследующийся от класса Person, представляющий сотрудника, имеющий следующие атрибуты:

- __slots__ = ('salary',): список атрибутов, доступных объекту.

Напишите класс Manager, наследующийся от класса Employee, представляющий менеджера, имеющий следующие атрибуты:

- __slots__ = ('bonus',): список атрибутов, доступных объекту.
"""


class Person:
    __slots__ = ('name', 'age')

    def __init__(self):
        self.name = 'name'
        self.age = 0


class Employee(Person):
    __slots__ = ('salary', )

    def __init__(self):
        super().__init__()
        self.salary = 0


class Manager(Employee):
    __slots__ = ('bonus', )

    def __init__(self):
        super().__init__()
        self.bonus = 0


person = Person()
person.name = "John"
person.age = 30
try:
    person.salary = 5000  # raises AttributeError
except AttributeError:
    print('raises AttributeError')

employee = Employee()
employee.name = "Jane"
employee.age = 25
employee.salary = 5000

manager = Manager()
manager.name = "Bob"
manager.age = 40
manager.salary = 10000
manager.bonus = 5000
