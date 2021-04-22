def tup_dict(tup, dict):
    for a, b in tup:
        dict.setdefault(a, []).append(b)
    return dict
        

tup = [("Reshma", 10), ("Bubbu", 12), ("Minion", 14), 
     ("andamay", 20), ("Bg", 25), ("Kathi", 30)]
dict = {}
print (tup_dict(tup, dict))


