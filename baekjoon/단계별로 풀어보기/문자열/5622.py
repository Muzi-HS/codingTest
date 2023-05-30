word = input()
time = 0
for i in word:
    j = ord(i)
    if j > 64 and j <68: #ABC
        time = time + 3
    elif j > 67 and j <71: #DEF
        time = time + 4
    elif j > 70 and j < 74: #GHI
        time = time + 5
    elif j > 73 and j < 77: #JKL
        time = time + 6
    elif j > 76 and j < 80: #MNO
        time = time + 7
    elif j > 79 and j < 84: #PQRS
        time = time + 8
    elif j > 83 and j < 87: #TUV
        time = time + 9
    else:
        time = time + 10

print(time)