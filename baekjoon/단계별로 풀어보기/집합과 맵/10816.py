import sys

input = sys.stdin.readline

n = int(input())
card = sorted(list(map(int,input().split())))
m = int(input())
checks = list(map(int,input().split()))

cnt = {}

for i in card:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
    
for check in checks:
    if check in cnt:
        print(cnt[check], end = ' ')
    else:
        print(0, end = ' ')