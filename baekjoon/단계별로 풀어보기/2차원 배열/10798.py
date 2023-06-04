import sys
input = sys.stdin.readline

a = [list(input().rstrip()) for _ in range(5)]

maximum = 0

for i in a:
    if len(i)>maximum:
        maximum = len(i)

for i in range(maximum):
    for j in range(5):
        try:
            print(a[j][i],end='')
        except:
            continue