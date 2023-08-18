import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
shift = list(map(int, input().split()))
balloons = deque()

for i in range(n):
    balloons.append(i+1)

pointer = 0

while balloons:
    balloon = balloons.popleft()
    print(balloon,end=' ')
    paper = shift[balloon-1]
    if paper>=0:
        balloons.rotate(-paper+1)
    else:
        balloons.rotate(-paper)