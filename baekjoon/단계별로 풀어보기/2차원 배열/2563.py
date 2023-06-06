import sys
input = sys.stdin.readline
n = int(input())

a = [[0]*100 for _ in range(100)]

for _ in range(n):
    x,y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            a[i][j] = 1

cnt=0
for i in range(0,100):
    for j in range(0,100):
        if a[i][j] == 1:
            cnt += 1

print(cnt)