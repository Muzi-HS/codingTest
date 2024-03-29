import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

q = deque()

for _ in range(n):
    command = list(map(str,input().split()))
    if len(command) > 1:
        q.append(int(command[-1]))
    else:
        if command[0] == 'pop':
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif command[0] == 'size':
            print(len(q))
        elif command[0] == 'empty':
            if q:
                print(0)
            else:
                print(1)
        elif command[0] == 'front':
            if q:
                print(q[0])
            else:
                print(-1)
        elif command[0] == 'back':
            if q:
                print(q[-1])
            else:
                print(-1)

