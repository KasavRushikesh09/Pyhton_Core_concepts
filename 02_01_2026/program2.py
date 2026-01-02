import timeit
# a = 70
# print(a)
# print("{0:x}".format(a))


''''    f string literal   '''
import math

#### def^n between format() , f string literal ####
#
# name = 'rushikesh'
# place = 'nashik'
# # print(f"{name} {place}")
# print("{} {}".format(name, place))
# print("{1} {0}".format(name, place))
#
# print("{0:.4f}".format(math.pi))
# print("hello {1},you are from {0} right".format(name,place))


# print(timeit.timeit(stmt = "{0:.2f}".format(3.1416),number = 10000))
# print(timeit.timeit(stmt = f"{3.1416:.2f}",number = 10000))
def pen(*pens):
    print(pens)
pen("red","black","blue","green")




