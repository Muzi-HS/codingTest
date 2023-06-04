import sys
input = sys.stdin.readline

a = [list(map(int, input().split())) for _ in range(9)]

m = a[0][0]
row =1
col =1
for i in range(9):
    for j in range(9):
        if a[i][j]>m:
            m = a[i][j]
            row = i+1
            col = j+1

print(m)
print("{} {}".format(row,col))