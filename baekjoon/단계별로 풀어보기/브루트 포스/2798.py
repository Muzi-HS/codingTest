n, m = map(int, input().split())
num = list(map(int, input().split()))

res=0

for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1, n):
            tmp = num[i]+num[j]+num[k]
            if res<tmp and tmp<=m:
                res = tmp

print(res)