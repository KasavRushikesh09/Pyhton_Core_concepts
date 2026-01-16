import re
#match()
'''print(re.match(r"hello","hello world"))
'''

#search()
'''print(re.search(r"world","hello world"))
'''

#findall()
'''print(re.findall(r"world","hello world"))
'''

#finditer()
'''for m in re.finditer(r"\d+","A1 B22 C333"):
    print(m.group(),m.start(),m.end())

'''

'''text = "I have 2 apples and 5 bananas"
matches = re.finditer(r"\d+",text)
for m in matches:
    print(m.group(),m.start(),m.end())
'''

#sub()
'''print(re.sub(r"\d+","#","A1 B22 C333"))'''

#split()
'''print(re.split(r"\s+","Hello World Python"))'''

#compile()
pattern = re.compile(r"\d+")
print(pattern.findall("I have 2 apples and 45 mangoes"))




