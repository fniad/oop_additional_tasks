# Для свойства balance используйте декоратор @property.

class BankAccount:

    def __init__(self, balance):
        """Конструктор, принимающий баланс"""
        self._balance = balance

    @property
    def balance(self):
        """Свойство, которое возвращает текущий баланс счета"""
        return self._balance

    @balance.setter
    def balance(self, balance):
        self._balance = balance

    def deposit(self, amount):
        """Метод, который позволяет внести деньги на счёт"""
        self.balance += amount

    def withdraw(self, amount):
        """Метод, который позволяет снять деньги со счета"""
        self.balance -= amount

    def close(self):
        """Метод, который закрывает счет и возвращает оставшиеся на нем деньги"""
        self.balance = 0


account = BankAccount(1000)
print(account.balance)  # 1000

account.deposit(500)
print(account.balance)  # 1500

account.withdraw(200)
print(account.balance)  # 1300

account.close()
print(account.balance)  # 0
