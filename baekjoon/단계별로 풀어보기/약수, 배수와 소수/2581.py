n = int(input())
m = int(input())
total = 0
arr=[]
for i in range(n,m+1):
    check = 0
    if i == 1:
        check=1
    for j in range(2,i):
        if i%j == 0:
            check=1
            break
    if check == 0:
        arr.append(i)
        total+=i

if total==0:
    print(-1)
else:
    print(total)
    print(arr[0])    
