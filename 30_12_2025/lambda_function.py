# ## with def function

# def power_of(num,p):
#     return num**p
# res = power_of(2,5)
# print(res)


# ## lambda function

# res= (lambda num,p : num**p)(2,5)
# print(res)
# class Hello:
#     def get_Quotient(self,num,den):
#       return num/den
# #    fun = lambda num,den : num/den
#     fun = lambda num,den : num/den
#     res = fun(100,2)
#     print(res)
   
# h=Hello()
# print(h.get_Quotient(100,2))

# fun = lambda num,den : num/den
# res = fun(100,2)
# print(res)

# res1 = fun(200,5)
# print(res1)

lst = [10,25,30,45,50,56]
def fun(c):
    if c%2 == 0:
        return True
    else:
        return False
    
res = list(filter(fun,lst))
print(res)


