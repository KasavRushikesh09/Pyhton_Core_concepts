# my_dict = {}
#
# for _ in range(3):
#     key = input("Enter the key : ")
#     value= int(input("Enter the value : "))
#     my_dict[key] = value
#
# print(my_dict)


my_dict2 = { input("Enter ID: "):{input("Enter Name"): input("Enter City: ")for _ in range(2)} for _ in range(3)}
print(my_dict2)

print("\n".join(f"{k} : {v}" for k,v in my_dict2.items()))