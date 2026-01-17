my_lst = []

for _ in range(10):
    my_lst.append(_+1)
print(my_lst)


my_lst2 = [_+1 for _ in range(10)]
print(my_lst2)