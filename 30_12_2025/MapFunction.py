lst = [1,2,3,4,5]

def fun(x):
    return x**2

sq_List = list(map(fun,lst))
print(sq_List)

# res = list(map(lambda x : x**2,lst))
# print(res)
# def fun1(num):
#     return lambda x : x**num
# # result = fun1(2)(4)
# # print(result)

# fun2 = fun1(3)
# print(fun2(5))
# x= int(input("Enter the number: "))
# count = 1

# mul = lambda x : count*x


# def fun1(num):
#     return lambda x : x*num
# math_table = fun1(6)

# for i in range(1,11):
#     print(math_table(i))

# def fun1(num):
#     return lambda x : x*num
# n = int(input("enter the number:\n"))
# math_table = fun1(n)

# for i in range(1,11):
#     print(n,"X",i,"=",math_table(i))

