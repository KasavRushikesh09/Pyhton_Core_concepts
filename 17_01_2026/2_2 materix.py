my_list = []

for i  in range(5):
    row = []
    for j in range(6):
        row.append(j+1)
    my_list.append(row)

for row in my_list:
    print(row)

