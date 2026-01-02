'''    program on strings 1  '''
import math
from functools import reduce

#
# s = input("Enter the string:  ")
#
# low_count,up_count,sp_count,num_count = 0,0,0,0
#
# for i in s:
#     if i.islower():
#         low_count += 1
#     elif i.isupper():
#          up_count +=1
#     elif  i.isnumeric():
#         num_count += 1
#     else:
#         sp_count += 1
#
# print("Lower case=",low_count)
# print("upper case=",up_count)
# print("sp case=",sp_count)
# print("num case=",num_count)

'''    program on string 2   '''
# s = input('Enter a string: ')
# s1 = s.swapcase()
# print(s1)


'''   program on string 3   '''
# s= input("Enter a string: ")
# s1 = s.swapcase()
# print(s1)
# s2 = s1.title()
# print(s2)
# s3 = s1.capitalize()
# print(s3)


'''   String translate   '''
# s = "Error 404 not found"
# table = s.maketrans("aeiou","AEIOU","0123456789")
# s_tables = s.translate(table)
# print(s_tables)

'''   String formating   '''
# name = input("Enter the name\n")
# place = input("Enter the place\n")
#
# s = "Hello {}, how are you? and you are from {}".format(name, place)
# print(s)

'''    format specification   '''
### right alignment###
# s = "{0:*>10}".format(999)
# print(s)

#### left alignment ###
# s = "{0:<10}".format(999)
# print(s)

##### center align ####
# s = "{0:*^11}".format(999)
# s = "{0:*^10}".format(990)
# print(s)

###   F.FIXED  Point notation ####
# s = "{0:010.4f}".format(math.pi)
# print(s)

# s = "{0},{1},{2}".format(*[10,11,12])
# print(s)


'''   program 1    '''
nums = input("Enter the numbers: ").split()
l = list(map(int,nums))
print(l)
res = reduce(lambda x,y : x+y ,l)
avg = res/len(l)
print(avg)

print("{0:.4f}".format(avg))
print("{0:^14.4f}.".format(avg))












