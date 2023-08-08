import sys
n = int(input())

info = []
for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    info.append([int(age),i,name])

info.sort()

for i in range(len(info)):
    print("%d %s"%(info[i][0],info[i][2]))
