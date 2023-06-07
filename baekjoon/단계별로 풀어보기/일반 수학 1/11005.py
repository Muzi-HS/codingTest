n, b = map(int, input().split())
res =[]
while True:
    r = n % b
    n = n // b
    if r>9:
        res.append(chr(r+55))
    else:
        res.append(r)
    if n ==0:
        break

for i in range(0,len(res)):
    print(res[len(res)-1-i],end='')
