import sys
from collections import deque

input = sys.stdin.readline

q = deque()

for _ in range(int(input())):
    command = list(map(int,input().split()))
    if len(command)>1:
        if command[0] == 1:
            q.appendleft(int(command[-1]))
        elif command[0] == 2:
            q.append(int(command[-1]))
    else:
        if command[0] == 3:
            if q:
                print(q.popleft())
            else:
                print(-1)
        elif command[0] == 4:
            if q:
                print(q.pop())
            else:
                print(-1)
        elif command[0] == 5:
            print(len(q))
        elif command[0] == 6:
            if q:
                print(0)
            else:
                print(1)
        elif command[0] == 7:
            if q:
                print(q[0])
            else:
                print(-1)
        elif command[0] == 8:
            if q:
                print(q[-1])
            else:
                print(-1)