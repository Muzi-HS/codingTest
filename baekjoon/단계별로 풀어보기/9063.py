import sys
n = int(input())
X = []
Y = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    X.append(x)
    Y.append(y)

xmin=X[0]
xmax=X[0]
for i in X:
    if i<xmin:
        xmin=i
    if i>xmax:
        xmax=i

ymin=Y[0]
ymax=Y[0]
for j in Y:
    if j<ymin:
        ymin=j
    if j>ymax:
        ymax=j

print((xmax-xmin)*(ymax-ymin))