"""
Напишите класс Bird, представляющий птицу, имеющий следующие методы:

- fly(self): метод, который выводит сообщение "Flying".

Напишите класс Penguin, наследующийся от класса Bird, представляющий пингвина, имеющий следующие методы:

- fly(self): метод, который выводит сообщение "I am a penguin and cannot fly".

Напишите класс Eagle, наследующийся от класса Bird, представляющий орла, имеющий следующие методы:

- hunt(self): метод, который выводит сообщение "Hunting".
"""


class Bird:
    def __init__(self):
        pass

    def fly(self):
        print('Flying')


class Penguin(Bird):
    def __init__(self):
        super().__init__()

    def fly(self):
        print('I am a penguin and cannot fly')


class Eagle(Bird):
    def __init__(self):
        super().__init__()

    def hunt(self):
        print('Hunting')


bird = Bird()
bird.fly()  # Flying

penguin = Penguin()
penguin.fly()  # I am a penguin and cannot fly

eagle = Eagle()
eagle.fly()  # Flying
eagle.hunt()  # Hunting
