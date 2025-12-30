
### Encapsulation

# class Account:
#     def __init__(self,bal,acc):
#         self.bal=bal
#         self.acc=acc

#     # @staticmethod
#     def debit(self,amount):
#         self.bal -= amount
#         # self.acc="MAHB000009"
#         print("Rs.",amount,"was debited")
#         print("Total balance = ", self.get_balance())

#     # @staticmethod
#     def credit(self,amount):
#         self.bal += amount
#         # self.acc="MAHB00009"
#         print("Rs.",amount,"was credited.")
#         print("Total balance = ", self.get_balance())

#     def get_balance(self):
#         return self.bal
# acc1 = Account(75000,986028)
# acc1.debit(1000)
# acc1.credit(500)

### delete 
# class Student:
#     def __init__(self,name):
#         self.name = name

# s1 = Student("shradha")
# del s1
# print(s1)
#### private (like) attribute and method

# class Student:
#     def __init__(self,name,roll_no):
#         self.name = name
#         self.__roll_no = roll_no
    
#     def reset_rollno(self):
#         print(self.__roll_no)
        

# stu1 = Student("Rushikesh",103)
# print(stu1.reset_rollno())
# print(stu1.name,stu1.__roll_no)

#Ex-2
# class Person:
#     __name = "Rushi"

#     def __hello(self):
#         print("hello guys")

#     def welcome(self):
#         self.__hello()
# p1 = Person()
# print(p1.welcome())
