import re
# text = ('''google
# gooogle
# goooogle
# gooooogle
# goooooogle
# gooooooogle
# goooooooogle''')
# regex = r"go{2,5}gle"
# result = (re.findall(regex,text))
# print(result)
# regex = r"\*"
# result = re.findall(regex,text)
# print(result)

#regex ="Python | easy"
# result = re.findall(regex,text)
# print(result)

# regex = r"P?ython"
# result = re.findall(regex,text)
# print(result)
#
# text = "hi,rushikesh how are you:909"
# regex = r"[a-zA-Z0-9]"
# result = re.findall(regex,text)
# print(result)

# text = "hi,rushikesh how are you:909"
# regex = r"\D"
# result = re.findall(regex,text)
# print(result)


text = "hi,rushikesh week how are weak you:909"
regex = r"we[ae]k"
result = re.findall(regex,text)
print(result)
