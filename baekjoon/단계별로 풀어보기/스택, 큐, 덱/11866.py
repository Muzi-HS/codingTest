import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int,input().split())

q = deque()

for i in range(n):
    q.append(i+1)

pointer = 1

print('<',end='')
while True:
    q.rotate(-k+1)
    print(q.popleft(),end='')
    if len(q)==0:
        print('>')
        break
    print(', ',end ='')
