# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, name: str, acc_number: str, balance: float):
        self.__name = name
        self.__acc_number = acc_number
        self.__balance = balance

    def deposit(self, amount: float):
        self.__balance = self.__balance + amount
        self.__service_charge()

    def withdraw(self, amount: float):
        if self.__balance > amount:

            self.__balance = self.__balance - amount
            self.__service_charge()
        else:
            raise ValueError("You don't have this amount in balance")

    @property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        self.__balance = self.__balance - (0.01 * self.__balance)

if __name__ == "__main__":

    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)