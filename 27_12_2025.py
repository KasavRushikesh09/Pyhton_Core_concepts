# QS -- Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Student:
    def __init__(self,name,subject1,subject2,subject3):
        self.name = name
        self.Math = subject1
        self.Eng = subject2
        self.His = subject3
    
s1 = Student("Rushikesh",92,88,74)
s2 = Student("aniket",78,99,34)
s3 = Student("pooja",77,48,89)

print(s1.name,s1.Math,s1.Eng,s1.His)
print(s2.name,s2.Math,s2.Eng,s2.His)
print(s3.name,s3.Math,s3.Eng,s3.His)