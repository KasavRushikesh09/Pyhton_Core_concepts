import re
'''    '|' meta charector   '''
# text = ("Python is super easy")
# regex = r"Python|super"
# l = re.findall(regex,text)
# print(l)

'''  '*' meta charector   '''
# text =" a whole hole is not a wwwhole"
# regex = r"w*hole"
# l = re.findall(regex,text)
# print(l)

'''    '?' meta charector   '''
# text = "a whole hole is not a wwwhole"
# regex = r"w?hole"
# l = re.findall(regex,text)
# print(l)

# text = "I know that no one is there in the school now"
# regex = r"k?now?"
# matches = re.findall(regex,text)
# print(matches)
# print("Number of occurrences = ",len(matches))

''' '+' meta charecter   '''
# text = "a whole hole is not a wwwhole"
# regex = r"w+hole"
# l = re.findall(regex,text)
# print(l)

'''  '$' meta charector   - match for ending'''
# text = "python has nothing to do  with the snake python"
# regex = r"python$"
# match  = re.search(regex,text)
# print(match)

'''   '^' meta charector  - match for first '''
# text = "python has nothing to do with the snake python"
# regex = r"^python"
# match = re.search(regex, text)
# print(match)

'''  '[]' meta charector '''
# text = "python java ai data science"
# regex = r"[aeiou]"
# match = re.findall(regex,text)
# print(len(match))


'''   '[a-zA-Z0-9]  meta charector  '''
# text =  "python java ai data science"
# regex = r"[a-zA-Z0-9]"
# match = re.findall(regex,text)
# print(len(match))

'''  '\w' meta charector   '''
# text = "hello my name is rushikesh :82087888892 "
# regex = r"\w"
# match = re.findall(regex,text)
# print(match)

'''   '\d' meta charector   '''
# text = "hello guys lets learn Python : 897447462910"
# regex = r"\d"
# match = re.findall(regex,text)
# print(match)

'''   '\w' meta charector   '''
# text = "hello guys lets learn Python : 897447462910"
# regex = r"\w"
# match = re.findall(regex,text)
# print(match)

'''   '{}' meta charector   '''
# text  =  "only the weak wait for the week to end"
# regex = r"we[ae]k"
# l = re.findall(regex,text)
# print(l)

# text = "Python is the best language four"
# regex = r"\b[a-zA-Z0-9]{4}\b"
# l = re.findall(regex ,text)
# print(l)

''' valid email address code  '''
# text='''ruhsikeshkasav1@gmail.com
# john.doe@gmail.com
#       user_123@company.co.in
#       test-email@domain.org
#       test-email@domain.org
#     firstname.lastname@outlook.com'''
# regex = r"[a-zA-Z0-9_$]+@gmail.com"
# result = re.findall(regex,text)
# print(result)

'''   gmail.com to rooman.com  '''
# text='''ruhsikeshkasav1@gmail.com
# john.doe@gmail.com
#       user_123@company.co.in
#       test-email@domain.org
#       test-email@domain.org
#     firstname.lastname@outlook.com'''
# regex  = r"@[a-zA-Z]+.com"
# match = re.sub(regex,"@rooman.com",text)
# print(match)

text  = ['98777844942', '982374224234','8208677782','9860262429']
p = re.compile(r"\b\d{5}[02468]\d{4}\b")
for i in text:
       if p.search(i) != None:
           print(i,"valid")
       else:
           print(i,"invalid")
regex = r"\d{10}"
print(re.search(regex,text))
print(re.findall(regex,text))


