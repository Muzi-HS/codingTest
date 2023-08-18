import sys

input = sys.stdin.readline

n = int(input())

stack = []

for _ in range(n):
    order = list(map(int,input().split()))

    if order[0] == 1:
        stack.append(order[-1])
        continue
    elif order[0] == 2:
        if stack:
            print(stack.pop())
            continue
        else:
            print(-1)
            continue
    elif order[0] == 3:
        print(len(stack))
        continue
    elif order[0] == 4:
        if stack:
            print(0)
            continue
        else:
            print(1)
            continue
    else:
        if stack:
            print(stack[-1])
            continue
        else:
            print(-1)
            continue
