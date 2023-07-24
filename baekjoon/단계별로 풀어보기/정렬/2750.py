n = int(input())

res = []

for _ in range(n):
    m = int(input())
    res.append(m)
res.sort()

for i in res:
    print(i)