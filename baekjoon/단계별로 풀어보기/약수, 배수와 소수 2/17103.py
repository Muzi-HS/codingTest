import sys

input = sys.stdin.readline

def prime(n):
    p = {}
    for i in range(0, n+1):
        p[i] = 1
    
    for i in range(2,int((n+1)**(1/2))+1):
        if p[i]>0:
            for j in range(i+i,n+1,i):
                p[j] = 0
    
    return p

t = int(input())

p = prime(1000000)

for _ in range(t):
    n = int(input())
    cnt = 0
    if n == 4:
        cnt += 1
        print(cnt)
        continue
    for i in range(3,n//2+1,2):
        if p[i] and p[n-i]:
            cnt += 1
    print(cnt)
