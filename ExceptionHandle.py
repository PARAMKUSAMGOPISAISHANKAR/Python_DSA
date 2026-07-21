# x=int(input("Enter a number: "))
# y=int(input("Enter a number: "))
# try:
#     print(x/y)
# except ZeroDivisionError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# finally:
#     print("Done")


# for i in range(5):
#     if i==4:
#         break
#     print(i)
# else:
#     print("Done")
    
# try :
#     a=int(input("Enter a Number: "))
#     print(a)
# except ValueError as e:
#     print(e)
# else:
#     print("Done")
    
    
# a=int(input("Enter a number: "))
# if a < 0:
#     raise ValueError("Number is Negative")
# else:
#     print(a)


#task 1
## keep asking vaild integer number
## if not valid integer number ,print error  -->
# while True:
#     try:
#         num = int(input("Enter an integer: "))
#         print("You entered:", num)
#         break
#     except ValueError:
#         print("Error: Please enter a valid integer.")
        
        
# <!-- # task 2
## handle index error while accessing list.
#elements is it is out of range handle it -->
# l=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# try:
#     print(l[10])
# except IndexError as e:
#     print(e)
    
    
# Access Modifiers
# class A:
#     def __init__(self, name, age, gender):
#         # Constructor
#         self._name = name      # Protected variable
#         self._age = age        # Protected variable
#         self.gender = gender   # Public variable
#     def display(self):
#         print(self._name)
#         print(self._age)
#         print(self.gender)

# a1 = A("Gopi Sai Shankar", 21, "Male")
# a1.setAge(22)  # Using the setter method to set age
# print(a1.display())  # Using the getter method to get age

# a2 = A("Ravi", 21, "Male")

# a1.display()
# a2.display()

# Abstraction
from abc import ABC, abstractmethod

# Abstract Base Class
# class BankAccount(ABC):
#     def __init__(self, balance):
#         self.__balance = balance  # Private variable

#     def deposit(self, amount):
#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             print("Insufficient Balance!")

#     def getBalance(self):
#         return self.__balance

#     @abstractmethod
#     def interestcalc(self):
#         pass


# # Child Class
# class SavingsAccount(BankAccount):
#     def interestcalc(self):
#         return self.getBalance() * 0.05


# # Create an object
# account = SavingsAccount(10000)

# print("Initial Balance:", account.getBalance())

# # Deposit money
# account.deposit(5000)
# print("Balance after Deposit:", account.getBalance())

# # Withdraw money
# account.withdraw(2000)
# print("Balance after Withdrawal:", account.getBalance())

# # Calculate Interest
# interest = account.interestcalc()
# print("Interest (5%):", interest)

# # Final Balance with Interest
# print("Balance after Adding Interest:", account.getBalance() + interest)


class Animal:
    print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Woof")
class Cat(Animal):
    def sound(self):
        print("Meow")