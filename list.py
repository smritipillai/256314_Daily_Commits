def change(my_list):
    for i in range(0,len(my_list),2):
        my_list[i],my_list[i+1]=my_list[i+1],my_list[i]
        return my_list

my_list = [1,2,3,4,5]

print(change(my_list))