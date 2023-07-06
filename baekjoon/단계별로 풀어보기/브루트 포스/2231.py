n = int(input())
res = n
for i in range(n-1,0,-1):
    total = i
    j = i
    while True:
        total += j%10
        j=j//10
        if j ==0:
            break
    if n == total and i<res:
        res = i
if res == n:
    print(0)
else:
    print(res)