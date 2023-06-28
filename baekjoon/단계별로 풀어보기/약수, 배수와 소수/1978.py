n = int(input())

m = list(map(int, input().split(' ')))

cnt = n

for _ in m:
    if _ ==1:
        cnt -=1
    for i in range(2,_):
        if _%i == 0:
            cnt -=1
            break

print(cnt)
