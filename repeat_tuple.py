tup = input()
rep = []
for i in tup:
    if tup.count(i) > 1:
        rep.append(i)
    else:
        continue

for i in rep:
    while rep.count(i)>1:
        rep.remove(i)

print("repeated numbers :", tuple(rep))
        