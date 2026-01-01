# lst = [1,2]
# i=0
# while i<1:
#     print(lst[i])
#     i += 1
# for i in lst:
#     print(i)
# print(lst[0])
# print(lst[1])
# print(lst[0])
# print(lst[1])
# print(lst[0])
# print(lst[1])
# print(lst[0])
# print(lst[1])

#for i in range(6):
#     print("python")

# print(range(5))

#print(list(range(2,10,2)))
#balance = 15000
# min_balance =  500
# print("Before Transaction : ",balance)
# for i in range(5):
#     balance = balance-1000
# print("after transaction : ",balance)
#num = int(input("Enter the number :\n"))
#
# for i in range(2,num+1):
#     if num%i == 0:
#         break
# if i == num:
#     print(num,"is prime")
# else:
#     print(num,"is not prime")
# n = int(input("Enter the num: "))
# def prime(n):
#     for i in range(2, n+1):
#         if n % i == 0:
#             print(n,"prime is not prime")
#         else:
#             print(n,"prime number")
# print(prime(n))
'''   prime number   '''
#num = int(input("Enter the number: "))
# for i in range(2,num+1):
#     if num%i == 0:
#         break
# if i == num:
#     print(num,"is prime number")
# else:
#     print(num,"is not prime number")
'''    odd and even sum '''
# even_sum,odd_sum = 0,0
# n = int(input("Enter the number:: "))
#
# for i in range(2,n+1):
#     if(i%2 == 0):
#         even_sum += i
#         continue
#     odd_sum +=i
# print("sum of all even numbers is: ",even_sum)
# print("sum of all odd num is: ",odd_sum)

'''    def-function   '''
# num = int(input("enter the number: "))
# p = int(input("enter the power number: "))
# def power(num,p):
#     return num**p
# res = power(num,p)
# print(res)

''' lambda function '''
# num = int(input("enter the number: "))
# p = int(input("enter the power number: "))
#
# res = (lambda num,p : num**p)(num,p)
#
# print(res)

'''   map() - function'''

'''lst = [1,2,3,4,5,6,7,8,9]
'''
'''def fun(x):
    return x**2'''

'''sq_lst = list(map(lambda x: x**2,lst ))
print(sq_lst)'''
#num = [1,2,3,4,5,6,7,8,9]
# def fun1(num):
#     return lambda x : x*num
# fun2 = fun1(4)
# print(fun2(5))

# n = int(input("Enter number: \n"))
# def table(n):
#     return lambda x : x*n
# math_fun = table(n)
#
# for i in range(1,11):
#     print(n,"X",i,"=",math_fun(i))







