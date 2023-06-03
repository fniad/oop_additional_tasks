class User:
    def __init__(self, name, password):
        """Конструктор, принимающий имя пользователя и пароль"""
        self._name = name  # свойство, которое возвращает имя пользователя
        self._password = password  # свойство, которое позволяет установить или изменить пароль пользователя
        self._is_admin = False  # свойство, которое возвращает, является ли пользователь администратором или нет

    @property
    def is_admin(self):
        return self._is_admin

    @is_admin.setter
    def is_admin(self, value):
        if not isinstance(value, bool):
            raise TypeError("Значение должно быть типа bool")
        self._is_admin = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name
        return self._name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        self._password = new_password
        return self._password

    def login(self, password):
        """метод, который проверяет, соответствует ли введенный пароль паролю пользователя"""
        if self.password == password:
            return True
        return False

    def logout(self):
        """Метод, который выходит из аккаунта пользователя"""
        self.name = None
        self.password = None


user1 = User("Alice", "qwerty")
print(user1.name)  # Alice
print(user1.password)  # qwerty
print(user1.is_admin)  # False

user1.password = "newpassword"
print(user1.password)  # newpassword

user1._is_admin = True
print(user1.is_admin)  # True

user1.login("newpassword")  # True
user1.logout()
