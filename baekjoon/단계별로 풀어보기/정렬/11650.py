n = int(input())

res = []
for _ in range(n):
    xy = list(map(int,input().split()))
    res.append(xy)

res.sort()

for xy in res:
    print("{} {}".format(xy[0],xy[1]))
