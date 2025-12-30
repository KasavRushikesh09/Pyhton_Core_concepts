
### Inheritance

# class Car:

#     @staticmethod
#     def start():
#         print("car started..")
#     @staticmethod
#     def stop():
#         print("car stopped..")

# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type = type

# car1 = Fortuner("disel")
# car1.start()

# ex2 ->

# class A:
#     varA = "welcome to class A"
# class B:
#     varB = "welcome to class B"
# class C(A,B):
#     varC = "welcome to class C"

# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# class Car:
#     def __init__(self,type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car Start..")

#     @staticmethod
#     def stop():
#         print("Car stopped..")

# class Toyota(Car):
#     def __init__(self,name,type):
#       super().__init__(type)
#       self.name = name
#       super().start()

# car1 = Toyota("nexus","electric")
# print(car1.type)

# class Person:
#     name = "anonymous"

#     @classmethod
#     # def changeName(self,name):
#         # Person.name = name
#         # self.__class__.name = "Rahul"
#     def changeName(cls,name):
#         cls.name = name
# p1 = Person()
# p1.changeName("rahul kumar")
# print(p1.name)
# print(Person.name)
# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property
#     def calcPercentage(self):
#         return str((self.phy+self.chem+self.math) /3)+"%"

# stu = Student(90,73,45)
# print(stu.calcPercentage)

# stu.phy = 34
# print(stu.calcPercentage)

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#     @property
#     def calcPercentage(self):
#         return str((self.math+self.phy+self.chem)/3+"%")
# stu = Student(99.78,65)
# stu.calcPercentage()

# stu.phy = 34
# print(stu.calcPercentage())

# print(1+2)   #3

# print("apna"+"college")  #concatenate

# print([1,2,3]+[4,5,6])   # merge
