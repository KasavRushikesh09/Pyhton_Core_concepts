
# class Student:
#     name = "Kiran"
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("craeting new student in database..")

# s1 = Student("kiran",97)
# print(s1.name, s1.marks)

# s2 = Student("arjun",88)
# print(s2.name,s2.marks)
# s2 = Student()
# print(s2.name)

# class Car:
#     color="blue"
#     brand= "mercedes"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

# n = int(input("Enter the value: "))
# total = 0

# for i in range(n):
#     num =int(input("Enter number: "))
#     total += num

# print("sum of all numbers: ",total)

# for i in range(1,100):
#     print(i)

# num = int(input("enter the num: "))

# count = 1

# while(count < 11):
#     ans = num*count
#     print(ans)
#     count +=1

# num = 5
# sum =0

# for i in range(1, num):
#     sum += i
# print(sum)


# num =5
# fact = 1
# i =1

# while(i<=num):
#     fact *= i
#     i +=1
# print(fact)

# num = 5
# fact = 1
# i = 1

# while(i<=num):
#     fact *= i
#     i += 1
# print(fact)
# class Student:
#     college_name = "ABC College"
#     name = "anonymous"

#     def __init__ (self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("Adding new student in Database..")

# S1 = Student("karan", 90)
# print(S1.name)

# class Student:
#     college_name = "Matoshri college"
#     name = "Rushikesh"

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         print("addinf new line in our database..")

# s1 = Student("kiran",90)
# print(s1.name)
# print(s1.marks)

# class Student:
#     college_name = "Matoshri College"

#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("Welcome student")
    
#     def get_marks(self):
#         return self.marks

# s1 = Student("karan",98)
# s1.welcome()
# print(s1.name,s1.marks)
# print(s1.get_marks())


# QS -- Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

# class Student:
#     def __init__(self,name,subject1,subject2,subject3):
#         self.name = name
#         self.Math = subject1
#         self.Eng = subject2
#         self.His = subject3
    
# s1 = Student("Rushikesh",92,88,74)
# s2 = Student("aniket",78,99,34)
# s3 = Student("pooja",77,48,89)

# print(s1.name,s1.Math,s1.Eng,s1.His)
# print(s2.name,s2.Math,s2.Eng,s2.His)
# print(s3.name,s3.Math,s3.Eng,s3.His)

# class Student :
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def hello():
#         print("hello")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi ",self.name,"your avg score is: ",sum/3)

# s1 = Student("tony stark",[99, 98, 97])
# s1.get_avg()


# class Student:
#     def __init__(self,name,marks):
#         self.name= name
#         self.marks= marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi,",self.name,"avg is:",sum/3)

# s1 = Student("tony stark",[99,89,66])
# s1.get_avg()


# Basic core Program:
#QS 1) ->
# name = input("enter the name: ")

# if len(name) < 3:
#       print("name must be atleast 3 char")
# else:
#       temp = "Hello <<UserName>>, How are you?"

#       output = temp.replace("<<UserName>>",name)
#       print(output)

#QS 2) ->
# import random
# n = int(input("Enter the number: "))

# if n <= 0:
#     print("give me positive integer")

# else:
#     heads = 0
#     tails = 0

#     for _ in range(n):
#         if(random.random() < 0.5):
#             heads += 1
#         else:
#             tails += 1
    

#     head_per = (heads/n)*100
#     tail_per = (tails/n)*100 

#     print(f"Heads: {head_per:.2f}%")
#     print(f"Tails: {tail_per:.2f}%")


# Qs 3 ->

# year = int(input("Enter the number: "))

# if(year < 999):
#     print("please enter 4 digits number")

# else:
#     if(year%400 == 0) or (year%4 == 0 and year%100 != 0):
#         print("Yes, this is Leap Year.")
#     else:
#         print("Not")

# year = int(input("enter the number"))

# if(year < 1000):
#     print("Invalid year ,year should be more than 999")

# else:
#     if(year%400 == 0)or(year%4 == 0 and year%100 != 0):
#         print("leap year")
#     else:
#         print("not")


#Qs - 4 ->

# p = int(input("Enter the number: "))
# N = int(input("Enter the power value N: "))

# if( N < 0 or N >= 31):
#     print("Please enter a value between 0 ans 30")
# else:
#     power = 1
#     for i in range(N+1):
#         print(f"{p}^{i} = {power}")
#         power = power * 2

#Qs - 5 ->
# N = int(input("Enter the harmonic value N: "))

# # Validate input
# if N == 0:
#     print("N must not be 0")
# else:
#     harmonic = 0.0

#     # Compute harmonic number
#     for i in range(1, N + 1):
#         harmonic += 1 / i

#     # Print result
#     print(f"The {N}th Harmonic Value is: {harmonic:.2f}")

# n = int(input("Enter the harmonic value n: "))

# if(n == 0):
#     print("n must not be 0")
# else:
#     harmonic = 0.0
    
#     for i in range(1,n+1):
#         harmonic += 1/i

#     print(f"the{n}th Harmonic number is: {harmonic:.5f}")

# N = int(input("Enter the number: "))

# if N <= 1:
#     print("Enter a number greater than 1")
# else:
#     print("prime factors are: ")

#     i = 2
#     while i * i <=N:
#         while n % i == 0:
#             print(i)
#             N = n // i
#         i += 1

#         if N > 1:
#             print(N)


# n = int(input("Enter the number: "))
# if( n<=1):
#     print("more than 1")
# else:
#     print("prime factor are: ")

#     i = 2
#     while i*i <=n:
#         while n%i ==0:
#             print(i)
#             n = n //2
#         i +=1

#         if(n > 1):
#             print(n)

# n = int(input("enter the number: "))

# i = 2
# while i*i <= n:
#     if(n%i == 0):
#         print(i)
#         n = n//i
#     else:
#         i += 1
# if n>1:
#     print(n)
# n = int(input("Eneter the number"))
# i=2
# while i*i <= n:
#     if(n%i == 0):
#         print(i)
#         n = n//i
#     else:
#         i +=1
# if(n>1):
#     print(n)


### Abstraction
# class Car:
#     def __init__(self):
#        self.acc = False
#        self.brk = False
#        self.clutch = False
#     def start(self):
#         self.clutch = True
#         self.acc =True
#         print("car strted..")
# car1 = Car()
# car1.start()

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





        











    
    

