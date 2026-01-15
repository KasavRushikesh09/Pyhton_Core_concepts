#import re
# text  = "9860262449 820867778"
# regex = r"\d{10}"
# print(re.search(regex,text))
# print(re.findall(regex,text))

import re
text = "9876543322  820867778"
p = re.compile(r"\d{10}")
print(type(p))
print(p.search(text))
print(p.findall(text))


