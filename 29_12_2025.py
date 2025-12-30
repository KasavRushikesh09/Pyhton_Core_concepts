
# print()
# class Complex:
#     def __init__(self,real,img): 
#         self.real = real
#         self.img = img
    
#     def showNumber(self):
#         print(self.real,"i +",self.img,"j")
     
#     def add(self,c2):
#         newReal = self.real + c2.real
#         newImg = self.real + c2.img

#         return Coplrx(newReal, nw)


# c1 = Complex(2,4)
# c1.showNumber()
# c2 = Complex(3,6)
# c2.showNumber()
# class Complex:
#     def __init__(self,real,img):
#         self.real = real
#         self.img = img

#     def showNumber(self):
#         print(self.real,"i +",self.img,"j")
    
#     def __add__(self,num2):
#         newReal = self.real + num2.real
#         newImg = self.img + num2.img
#         return Complex(newReal, newImg)
    
#     def __sub__(self,num2):
#         newReal = self.real - num2.real
#         newImg = self.img - num2.img
#         return Complex(newReal, newImg)
    
#     def __mul__(self,num2):
#         newReal = self.real*num2.real
#         newImg = self.img*num2.img
#         return Complex(newReal,newImg)
    
#     def __truediv__(self,num2):
#         newReal = self.real / num2.real
#         newImg = self.img / num2.img
#         return Complex(newReal,newImg)
    
#     def __mod__(self,num2):
#         newReal = self.real % num2.real
#         newImg = self.img % num2.img
#         return Complex(newReal,newImg)

# num1 = Complex(4,8)
# num1.showNumber()

# num2 = Complex(2,3)
# num2.showNumber()

# print("added numbers: ")
# num3 = (num1+num2)
# num3.showNumber()

# print("subtracted numbers: ")
# num4 = (num1-num2)
# num4.showNumber()

# print("multipled numbers: ")
# num5 =(num1*num2)
# num5.showNumber()

# print("Divide numbers: ")
# num6 =(num1/num2)
# num6.showNumber()

# print("Mod Of numbers: ")
# num7 = (num1%num2)
# num7.showNumber()

# class Dog:
#     def speak(self):
#         print("Bark")

# class Cat:
#     def speak(self):
#         print("mwow")

# def make_sound(animal):
#     animal.speak()

# make_sound(Dog())
# make_sound(Cat())

# class Box:
#     def __init__(self,value):
#         self.value = value
    
#     def __add__(self,other):
#         return self.value + other.value
    
# b1 = Box(10)
# b2 = Box(20)
# print(b1+b2)
# class Animal:
#     def sound(self):
#         print("Animal sound")

# class Dog(Animal):
#     def sound(self):
#         print("Barks")

# d1 = Dog()
# d1.sound()
# class Circle:
#     pi = 3.14

#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         area = Circle.pi * self.radius*self.radius
#         return area
    
#     def perimeter(self):
#         perimeter = Circle.pi * 2 * self.radius
#         return perimeter

# c = Circle(3)
# print(c.area())
# print(c.perimeter())

# class Circle:
#     pi = 3.14
#     def __init__(self,radius):
#         self.radius = radius

#     def area(self):
#         area = Circle.pi *self.radius*self.radius
#         return area
    
#     def  perimeter(self):
#         perimeter = Circle.pi *2*self.radius
#         return perimeter

# c = Circle(3)
# print(c.area())
# print(c.perimeter())

## QS - 1] -> 

# n = int(input("Enter the size of array: "))
# arr = list(map(int,input("enter elemenets: ").split()))

# triplets = []

# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if arr[i] + arr[j] + arr[k] == 0:
#                 triplet = sorted([arr[i], arr[j], arr[k]])
#                 if triplet not in triplets:
#                     triplets.append(triplet)

# print("Number of distinct triplets: ", len(triplets))
# print("Distinct triplets:")
# for t in triplets:
#     print(t)


# n = int(input("Enter the size of array: "))
# arr = list(map(int,input("enter elements: ").split()))

# triplets = []

# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if arr[i] + arr[j]+ arr[k] == 0:
#                 triplet = sorted([arr[i],arr[j],arr[k]])

#                 if triplet not in triplets:
#                     triplets.append(triplet)

# print("Number of distinct triplets: ",len(triplets))
# print("Distinct triplets:")
# for t in triplets:
#     print(t)


# m = int(input("Enter number of rows: "))
# n = int(input("Eneter number of columns: "))

# arr = []

# print("Enter elements:")
# for i in range(m):
#     row = []
#     for j in range(n):
#             row.append(int(input()))
#     arr.append(row)

# print("2D Array Output: ")
# for row in arr:
#         for val in row:
#             print(val,end=" ")
#         print()

# try :
# try:
#     a = int(input("enter number: "))
#     b = 10/a
#     print(b)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Invalid input")


# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("Invalid input")
# try:
#     x = 10
#     y = 2
#     print(x / y)
# except ZeroDivisionError:
#     print("Error")
# else:
#     print("Execution successful")