'''   empty string '''
from shlex import join

# s1 =''
#print(s1)

'''   single charector string  '''
# s2 = 'R'
# print(s2)

'''    combination of charector   '''
# s1 = "Rushikesh"
# print(s1)

'''    multiline string  '''
# s1 = ('''python
# java
# c++
# python''')
# print(s1)

'''   a real number convert to string '''
# s1 = str(99.9)
# print(s1)
# print(type(s1))

# s = '''"practice" make man \'perfect\''''
#print(s)
#
# s1 = "hello"
# s2 = "world"
# print(s1)
# print(s2)
# print(id(s1))
# print(id(s2))
# print(id(s1[4]))
# print(id(s2[1]))

'''    string slicing  '''
# s = "guido van rossum"
# print(s)
# print(s[10])
# print(s[0:5])
# print(s[-1:-7:-1])
# print(s[::-1])


''' program on strings'''
# s = input("Enter the string \n")
# for i in range(0,len(s)-1):
#     print(s[i:i+3])

# s = input("Enter your string:\n")
#
# for i in range(0,len(s)-2):
#     print(s[i:i+3])

'''   program on string2 '''
# s = input("Enter the string: \n")
# print(s[1:len(s)-1:1])

'''   program on string 3   '''
# s = input("Enter a string: \n")
# print(s[len(s)-2:0:-1])

'''   program on string 4 '''
# # s = input("Enter a string: \n")
# # if s==s[::-1]:
# #     print("This is palindrome")
# # else:
# #     print("Not a palindrome")
#
#
# # s  = "hello"+"world"
# # print(s)
# s1="hello"
# print(s1)
# s1 = s1+"world"
# print(s1)

# c = "a"
# print(chr(ord(c)-32))

# s = input("enter string: \n")
# s_upper=""
# for i in s:
#     if ord(i)>= 97 and ord(i) <= 122:
#         s_upper += chr(ord(i)-32)
#     else:
#         s_upper += i
#
# print(s)
# print(s_upper)

# s = input("Enter the number: ")
# s_upper = ""
# for i in s:
#     if ord(i) >= 97 and ord(i) <=122:
#         s_upper += chr(ord(i)-32)
#     else:
#         s_upper += i
# print(s_upper)
#ord function convert from char to ascii value

# s = input("Enter the String: ")
# s_upper = s.upper()
# print(s_upper)
# for i in s:
#     if ord(i) >= 97 and ord(i) <= 122:
#         s_upper += chr(ord(i)-32)
#     else:
#         s_upper += i
# print(s_upper)
# s_plan = s[:(len(s)//2):]
# print(s_plan)
# s_rev = s[len(s)-1:(len(s)//2)-1:-1]
# print(s_rev)
#
# print(s_plan+s_rev)

'''  reverse the half string  '''
# s = "Rushikesh"
# s_plan = s[0:len(s)//2:1]
# print(s_plan)
#
# s_half_rev = s[-1:len(s)//2-1:-1]
# print(s_half_rev)
#
# print(s_plan + s_half_rev)

# lst = ["rushi","urban","monkey","slice"]
# s = "".join(lst)
# print(s)
#
# url = ["http://www.example.com",
#        "https://www.github.com",
#        "http://www.wikipedia.org",
#        "https://www.stackoverflow.com",
#        "https://www.medium.com"]

# for i in url:
#     if i[0:5:1] == "https":
#         print(i)
#
# for i in url:
#     if i.startswith("https"):
#         print(i)
# for i in url:
#     if i.endswith(".com"):
#         print(i)


'''    join()   '''
# lst = ["java","python","c++","c#","c","c++","java"]
# s = join(lst)
# print(s)















