import sys
n = int(input())
res = []
for _ in range(n):
    xy = list(map(int, sys.stdin.readline().split()))
    yx = []
    yx.append(xy[1])
    yx.append(xy[0])
    res.append(yx)

res.sort()

for yx in res:
    print("{} {}".format(yx[1],yx[0]))
