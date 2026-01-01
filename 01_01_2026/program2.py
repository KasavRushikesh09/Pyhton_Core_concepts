
'''  filter() function '''
from functools import reduce

# lst = [1,2,3,4,56,7,8,8,90]
#
# #def fun(x):
# #     if(x%2 == 0):
# #         return True
# #     else:
# #         return False
# evn_lst = set(filter(lambda x : x%2 ==1,lst))
#
# print(evn_lst)

'''    reduce() function '''

# lst = [1,2,3,4,5,6,78,9]
# def fun(x,y):
#     return x*y

# res = reduce(lambda x,y : x+y,lst)
# print(res)
# res = reduce(fun,lst)
# print(res)

# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return n*fact(n-1)
#
# num = int(input("Enter a number: "))
# print(fact(num))
# def fact(n):
#     if(n == 1):
#         return 1
#     else:
#         return n*fact(n-1)
# num = int(input("Enter a number: "))
# print(fact(num))

'''   global variable/ global scope   '''

# x = 99
# print(x)
# def fun():
#     y =999
#     print(y)
#     print(x)
# fun()

'''   local variable / local scope'''
# x =99
# print(x)
# def fun():
#     y = 999
#     print(y)
#     print(globals())
#     print(locals())
# fun()
# print(x)

def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)
num = int(input("Enter the number: \n"))
print(fact(num))

