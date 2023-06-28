n = int(input())
k=2
while(n>1):
    if n % k == 0:
        print(k)
        n = n//k
        continue
    else:
        k += 1
