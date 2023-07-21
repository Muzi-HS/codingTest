n = int(input())

a = n // 5
b = n // 3
res = b+1
flag = 0
for i in range(b+1):
    for j in range(a+1):
        if 5*j+3*i == n and i+j<res:
            flag =1
            res = i+j
if flag == 0:
    print(-1)
else:
    print(res)