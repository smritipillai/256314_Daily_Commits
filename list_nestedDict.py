my_list = [1, 2, 3]
new_dict = {}
temp = new_dict
for i in my_list:
    temp[i] = {}
    temp = temp[i]
print(new_dict)