a = int(input("number A: "))
b = int(input("number B: "))
c = int(input("number C: "))

if a > b and a > c:
    print(a)
elif b > c and b > a:
    print(b)
else:
    print(c)