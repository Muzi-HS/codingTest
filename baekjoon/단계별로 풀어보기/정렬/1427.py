n = input()
res = []
for i in n:
    res.append(int(i))

res.sort()

for i in range(len(res)-1,-1,-1):
    print(res[i],end='')