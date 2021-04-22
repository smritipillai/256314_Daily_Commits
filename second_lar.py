my_list = input()
 
firstmax = max(my_list[0],my_list[1])
secondmax = min(my_list[0],my_list[1])
n = len(my_list)
for i in range(2,n):
    if my_list[i] > firstmax:
        secondmax = firstmax
        firstmax = my_list[i]
    elif my_list[i]>secondmax and firstmax != my_list[i]:
        secondmax = my_list[i]
 
print("Second highest number is : ", secondmax)