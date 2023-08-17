import sys

input = sys.stdin.readline

n = int(input())

windows = [0]*(n+1)

for i in range(2,n+1):
    if windows[i] == 0:
        for j in range(i+i,n+1,i):
            windows[j] = 1

print(sum(windows)+1)
