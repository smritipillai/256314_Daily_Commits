y = int(input("Input a year: "))

if (y % 400 == 0): #Checking for leap year
    lp = True
elif (y % 100 == 0):
    lp = False
elif (y % 4 == 0):
    lp = True
else:
    lp = False

m = int(input("Input a month from 1-12: "))

if m in (1, 3, 5, 7, 8, 10, 12):
    m_len = 31
elif m == 2:
    if lp:
        m_len = 29
    else:
        m_len = 28
else:
    m_len = 30


day = int(input("Input a day from 1-31: "))

if day < m_len:
    day += 1
else:
    day = 1
    if m == 12:
        m = 1
        y += 1
    else:
        m += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (y, m, day))