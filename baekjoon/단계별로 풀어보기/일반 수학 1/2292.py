n = int(input())

k = 0
total = 1
cnt = 0
while(True):
    cnt += 1
    total = total + k*6
    if total>=n:
        break
    k = k+1

print(cnt)