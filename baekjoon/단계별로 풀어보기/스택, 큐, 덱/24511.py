import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
qstackinfo = deque(map(int,input().split()))
arr = deque(map(int,input().split()))
m = int(input())
component = deque(map(int,input().split()))

res = deque()

for i in range(n):
    if qstackinfo[i] == 0:
        res.appendleft(arr[i])

for i in component:
    res.append(i)
    print(res.popleft(), end =' ')